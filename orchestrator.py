from os import environ as env

from Core.Devops.main import Main

"""
New | Approved | Committed | Test | Accepted | Review | Done
"""
PBI_STATES: str = "Committed Test Accepted Review"
APPROVEDS_COMMENTS: str = (
    "pre:aprovada pre:aprovado pré:aprovado pré:aprovada prod:aprovado prod:aprovada"
)

env["state"] = PBI_STATES
env["approveds_comments"] = APPROVEDS_COMMENTS


Main.main()
