from app.backlog import GetBacklogs
from app.excel import Excel
from app.treatment import Treatment
from app.login import Login
from app.comments import Comments


class Manager():
    @classmethod
    def run_pipeline(cls, mail_, pass_, states):
        Excel.remove_xls()
        Login.authenticate(mail_, pass_)
        backlogs: tuple = GetBacklogs.get_backlogs(states)
        Comments.validate_backlogs(backlogs)
        backlogs_treated = Treatment.remove_garbage(backlogs)
        Login.quit_driver()
        Excel.get_relatorio(backlogs_treated)