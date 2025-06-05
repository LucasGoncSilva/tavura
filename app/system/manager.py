from logging import Logger, getLogger
from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from app.auth.login import Login
from app.system.backlog import GetBacklogs
from app.system.comments import Comments
from app.system.excel import Excel
from app.system.treatment import Treatment


logger: Logger = getLogger('tavura')


class Manager:
    @classmethod
    def run_pipeline(
        cls: type[Self], mail: str, passwrd: str, states: list[str]
    ) -> None:
        """
        Orchestrates the automation flow, step by step.

        Going step by step, this method defines the flow for the entire automation,
        following the following:

            - Old report dealing
            - Bot auth using user credentials
            - Backlogs tracking based on `states` defined
            - Comments sanitization
            - Garbage removing
            - Report generation

        :param mail: User login email
        :type mail: str
        :param passwrd: User login password
        :type passwrd: str
        :param states: PBIs states to be tracked
        :type states: list[str]
        :returns: None.
        :rtype: None
        :raises: None
        """

        logger.info('Handling old report version')
        Excel.remove_xls()

        logger.info('Authenticating into system')
        Login.authenticate(mail, passwrd)

        logger.info('Tracking PBIs')
        backlogs: list[list[dict[str, str]] | list[WebElement | str]] = (
            GetBacklogs.get_backlogs(states)
        )

        logger.info('Confirming each PBI')
        backlogs_validated: list[dict[str, str | WebElement]] = (
            Comments.validate_backlogs(backlogs)
        )

        logger.info('Removing garbage')
        backlogs_treated: list[dict[str, str | WebElement]] = Treatment.remove_garbage(
            backlogs_validated
        )

        logger.info('Ending stuff and generating report')
        Login.quit_driver()
        Excel.get_relatorio(backlogs_treated)
