from app.manager import Manager
from app.constants import Constants
from app import constants

checks = "Committed Test"

Manager.run_pipeline(constants.MAIL, constants.PASS, checks) # type: ignore