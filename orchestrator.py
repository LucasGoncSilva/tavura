from app.system import constants
from app.system.manager import Manager


checks = 'Review Committed Test'

Manager.run_pipeline(constants.MAIL, constants.PASS, checks)
