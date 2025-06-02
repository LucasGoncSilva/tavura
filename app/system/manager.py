from logging import Logger, getLogger

from selenium.webdriver.remote.webelement import WebElement

from app.auth.login import Login
from app.system.backlog import GetBacklogs
from app.system.comments import Comments
from app.system.excel import Excel
from app.system.treatment import Treatment


logger: Logger = getLogger('tavura')


class Manager:
    @classmethod
    def run_pipeline(cls, mail_: str, pass_: str, states: list[str]) -> None:
        logger.info('Handling old report version')
        Excel.remove_xls()

        logger.info('Authenticating into system')
        Login.authenticate(mail_, pass_)

        logger.info('Tracking PBIs')
        backlogs: list[dict[str, str | WebElement]] = GetBacklogs.get_backlogs(states)

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
