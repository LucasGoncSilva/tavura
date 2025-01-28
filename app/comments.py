from app import constants
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class Comments():
    @classmethod
    def validate_backlogs(cls) -> None:
        approved_comments: list[str] = str(constants.APPROVEDS_COMMENTS).split()
        action = ActionChains(cls.driver)
        wait = WebDriverWait(cls.driver, 10)

        for backlog in cls.backlogs_element:
            cls.driver.implicitly_wait(.3)
            try:
                wait.until(element_to_be_clickable(backlog))
                action.move_to_element(backlog).click().perform()
                cls.comments: list[WebElement] = cls.driver.find_elements(
                    By.XPATH, constants.COMMENTS
                )
                cls.total_checked += 1
            except Exception as e:
                print(f"An error ocurred: {str(e)}")
                cls.total_checked += 1

            try:
                feature = cls.driver.find_element(
                    By.XPATH, constants.FEATURES
                )
            except:
                feature = " "

            if feature != " ":
                if "11119" in feature.text: # type: ignore
                    pbi = cls.get_pbi(backlog.text)
                    if pbi:
                        pbi.update({"FEATURE": "SIM"})

            for approved in approved_comments:
                """Obtenção da PBI e adiciona OK em status"""
                if any(
                    approved in comment.text.lower().replace(" ", "")
                    for comment in cls.comments
                ):
                    pbi = cls.get_pbi(backlog.text)
                    if pbi:
                        if "pre" in approved:
                            pbi.update({"STATUS": "PRE: OK"})
                        elif "prod" in approved:
                            pbi.update({"STATUS": "PROD: OK"})
            cls.driver.back()