from os import environ as env

from dotenv import load_dotenv

load_dotenv()

MAIL = env.get("MAIL")
PASS = env.get("PASS")

class Constants():
    @classmethod
    def get_fields(cls, number):
        FIELD_NUMBERS: str = f'//div[@class="flex-column flex-grow kanban-board-column padding-bottom-8"][{number}]/div/div/span/a/span[2]'
        FIELD_TITLES: str = f'//div[@class="flex-column flex-grow kanban-board-column padding-bottom-8"][{number}]/div/div/span/a/span[3]'
        FIELD_EFFORT: str = f'//div[@class="flex-column flex-grow kanban-board-column padding-bottom-8"][{number}]/div/div/div/div[2]'
        return (FIELD_NUMBERS, FIELD_TITLES, FIELD_EFFORT)
    
backlogs_states: list = [
    "New",
    "Approved",
    "Committed",
    "External",
    "Test",
    "Accepted",
    "Review",
    "Done",
]
    
COMMENTS: str = "//div[@class='comment-item flex-row displayed-comment depth-8 markdown-discussion-comment']/div[2]/div/div[2]"
FEATURES: str = "//div[@class='artifact-link-id secondary-text margin-right-4']"

SUSTENTACAO: str = "Sustentação - |Sustentação-|Sustentação -|Sustentação- |sustentação - |sustentação-|sustentação -|sustentação- |sustentacao - |sustentacao-|sustentacao- |sustentacao -|sustentacão - |sustentacao-|sustentacao- |sustentacao -|- Q1|- Q2|- Q3|-Q1|-Q2|-Q3| Q1|Q 1|Q - 1|Q-1|Q -1|Q-|q1|q 1|q - 1|q-1|q -1| Q1| Q 1| Q - 1| Q-1| Q -1| Q- 1| q1| q 1| q - 1| q-1| q -1|____|Q2|Q 2|Q - 2|Q-2|Q -2|Q- 2|q2|q 2|q - 2|q-2|q -2| Q2| Q 2| Q - 2| Q-2| Q -2| Q- 2| q2| q 2| q - 2| q-2| q -2|____|Q3|Q 3|Q - 3|Q-3|Q -3|Q- 3|q3|q 3|q - 3|q-3|q -3| Q3| Q 3| Q - 3| Q-3| Q -3| Q- 3| q3| q 3| q - 3| q-3| q -3|"
