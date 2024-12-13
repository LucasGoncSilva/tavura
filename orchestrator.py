from os import environ as env

from Core.aplication import Aplication
from Core.main import Main

"""
New Approved Committed External Test Accepted Review Done
"""
PBI_STATES: str = "Committed Test Accepted Review"


env["state"] = PBI_STATES

Main.main()
# Aplication()