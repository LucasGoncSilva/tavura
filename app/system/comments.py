from logging import Logger, getLogger
from typing import Literal

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait

from app.auth.login import Login
from app.system.constants import APPROVEDS_COMMENTS, COMMENTS, FEATURES


logger: Logger = getLogger('tavura')


class Comments(Login):
    @classmethod
    def validate_backlogs(
        cls, backlogs: list[dict[str, str | WebElement]]
    ) -> list[dict[str, str | WebElement]]:
        comments: list[WebElement] = []
        action: ActionChains = ActionChains(cls.driver)
        wait = WebDriverWait(cls.driver, 10)
        feature: WebElement | Literal[' ']

        for i in range(0, len(backlogs[0])):
            logger.debug(f'Confirming PBI {backlogs[0][i]["PBI"]}')

            backlog = backlogs[1][i]

            cls.driver.implicitly_wait(3)
            wait.until(element_to_be_clickable(backlog))

            cls.driver.execute_script(  # type: ignore
                "arguments[0].scrollIntoView({block: 'center'});", backlog
            )

            action.move_to_element(backlog).click().perform()
            comments = cls.driver.find_elements(By.XPATH, COMMENTS)

            try:
                feature = cls.driver.find_element(By.XPATH, FEATURES)
            except Exception:
                feature = ' '

            if feature != ' ' and '11119' in feature.text:
                pbi = cls.get_pbi(backlog.text, backlogs[0])
                if pbi:
                    pbi.update({'FEATURE': 'SIM'})

            for approved in APPROVEDS_COMMENTS:
                """Obtenção da PBI e adiciona OK em status"""
                if any(
                    approved in comment.text.lower().replace(' ', '')
                    for comment in comments
                ):
                    pbi = cls.get_pbi(backlog.text, backlogs[0])
                    if pbi:
                        if 'pre' in approved:
                            pbi.update({'STATUS': 'PRE: OK'})
                        elif 'prod' in approved:
                            pbi.update({'STATUS': 'PROD: OK'})
            cls.driver.back()
        return backlogs[0]

    @classmethod
    def get_pbi(
        cls, number: str, backlogs: list[dict[str, str | WebElement]]
    ) -> dict[str, str] | None:
        pbi = next((pbi for pbi in backlogs if pbi['PBI'] == number), None)
        return pbi
