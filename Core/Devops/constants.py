from os import environ as env

from dotenv import load_dotenv

load_dotenv()

MAIL = env.get("MAIL")
PASS = env.get("PASS")

NEW_NUMBERS: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][1]/div/div/span/a/span[2]"
NEW_TITLES: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][1]/div/div/span/a/span[3]"
NEW_EFFORT: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][1]/div/div/div/div[2]"

APPROVED_NUMBERS: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][2]/div/div/span/a/span[2]"
APPROVED_TITLES: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][2]/div/div/span/a/span[3]"
APPROVED_EFFORT: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][2]/div/div/div/div[2]"

COMMITTED_NUMBERS: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][3]/div/div/span/a/span[2]"
COMMITTED_TITLES: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][3]/div/div/span/a/span[3]"
COMMITTED_EFFORT: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][3]/div/div/div/div[2]"

TEST_NUMBERS: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][4]/div/div/span/a/span[2]"
TEST_TITLES: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][4]/div/div/span/a/span[3]"
TEST_EFFORT: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][4]/div/div/div/div[2]"

ACCEPTED_NUMBERS: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][5]/div/div/span/a/span[2]"
ACCEPTED_TITLES: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][5]/div/div/span/a/span[3]"
ACCEPTED_EFFORT: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][5]/div/div/div/div[2]"

REVIEW_NUMBERS: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][6]/div/div/span/a/span[2]"
REVIEW_TITLES: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][6]/div/div/span/a/span[3]"
REVIEW_EFFORT: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][6]/div/div/div/div[2]"

DONE_NUMBERS: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][7]/div/div/span/a/span[2]"
DONE_TITLES: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][7]/div/div/span/a/span[3]"
DONE_EFFORT: str = "//div[@class='flex-column flex-grow kanban-board-column padding-bottom-8'][7]/div/div/div/div[2]"

COMMENTS: str = "//div[@class='comment-item flex-row displayed-comment depth-8 markdown-discussion-comment']/div[2]/div/div[2]"
FEATURES: str = "//div[@class='artifact-link-id secondary-text margin-right-4']"

SUSTENTACAO: str = "Sustentação - |Sustentação-|Sustentação -|Sustentação- |sustentação - |sustentação-|sustentação -|sustentação- |sustentacao - |sustentacao-|sustentacao- |sustentacao -|sustentacão - |sustentacao-|sustentacao- |sustentacao -|Q1|Q 1|Q - 1|Q-1|Q -1|Q-|q1|q 1|q - 1|q-1|q -1| Q1| Q 1| Q - 1| Q-1| Q -1| Q- 1| q1| q 1| q - 1| q-1| q -1|____|Q2|Q 2|Q - 2|Q-2|Q -2|Q- 2|q2|q 2|q - 2|q-2|q -2| Q2| Q 2| Q - 2| Q-2| Q -2| Q- 2| q2| q 2| q - 2| q-2| q -2|____|Q3|Q 3|Q - 3|Q-3|Q -3|Q- 3|q3|q 3|q - 3|q-3|q -3| Q3| Q 3| Q - 3| Q-3| Q -3| Q- 3| q3| q 3| q - 3| q-3| q -3|"
