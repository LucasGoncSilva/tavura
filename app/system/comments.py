from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from app.auth.login import Login
from app.system import constants
from time import sleep


class Comments(Login):
    @classmethod
    def validate_backlogs(cls, backlogs) -> dict:
        comments = []
        approved_comments: list[str] = str(constants.APPROVEDS_COMMENTS).split()
        action = ActionChains(cls.driver)
        wait = WebDriverWait(cls.driver, 10)

        for backlog in backlogs[1]:
            cls.driver.implicitly_wait(.3)
            wait.until(element_to_be_clickable(backlog))
            cls.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", backlog)
            #sleep(.3)
            action.move_to_element(backlog).click().perform()
            comments = cls.driver.find_elements(
                By.XPATH, constants.COMMENTS
            )

            try:
                feature = cls.driver.find_element(
                    By.XPATH, constants.FEATURES
                )
            except:
                feature = " "

            if feature != " ":
                if "11119" in feature.text:
                    pbi = cls.get_pbi(backlog.text, backlogs[0])
                    if pbi:
                        pbi.update({"FEATURE": "SIM"})

            for approved in approved_comments:
                """Obtenção da PBI e adiciona OK em status"""
                if any(
                    approved in comment.text.lower().replace(" ", "")
                    for comment in comments
                ):
                    pbi = cls.get_pbi(backlog.text, backlogs[0])
                    if pbi:
                        if "pre" in approved:
                            pbi.update({"STATUS": "PRE: OK"})
                        elif "prod" in approved:
                            pbi.update({"STATUS": "PROD: OK"})
            cls.driver.back()
        return backlogs[0]

    @classmethod
    def get_pbi(cls, number, backlogs) -> dict | None:
        pbi = next((pbi for pbi in backlogs if pbi["PBI"] == number), None)
        return pbi