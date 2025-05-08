from selenium.webdriver.remote.webelement import WebElement

from app.auth.login import Login
from app.system.backlog import GetBacklogs
from app.system.comments import Comments
from app.system.excel import Excel
from app.system.treatment import Treatment


class Manager:
    @classmethod
    def run_pipeline(cls, mail_: str, pass_: str, states: str) -> None:
        Excel.remove_xls()
        Login.authenticate(mail_, pass_)
        backlogs: list[dict[str, str | WebElement]] = GetBacklogs.get_backlogs(states)
        backlogs_validated: list[dict[str, str | WebElement]] = (
            Comments.validate_backlogs(backlogs)
        )
        backlogs_treated: list[dict[str, str | WebElement]] = Treatment.remove_garbage(
            backlogs_validated
        )
        Login.quit_driver()
        Excel.get_relatorio(backlogs_treated)
