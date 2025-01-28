from app.system.manager import Manager
from app.system.constants import Constants
from app.system import constants

checks = "Committed Test"

Manager.run_pipeline(constants.MAIL, constants.PASS, checks)