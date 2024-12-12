from os import environ as env

from Core.main import Main

"""
New Approved Committed External Test Accepted Review Done
"""
PBI_STATES: str = "Committed Test"


env["state"] = PBI_STATES
Main.main()