from os import environ as env
from re import compile, IGNORECASE, VERBOSE
from dotenv import load_dotenv


load_dotenv()

MAIL: str | None = env.get('MAIL')
PASS: str | None = env.get('PASS')

if any(map(lambda x: x is None, [MAIL, PASS])):
    raise TypeError(
        f'Expected "MAIL" and "PASS" to be string, got "{type(MAIL)}", "{type(PASS)}"'
    )


class Constants:
    @classmethod
    def get_fields(cls, number: int) -> tuple[str, str, str]:
        FIELD_NUMBERS: str = f'//div[@class="flex-column flex-grow kanban-board-column padding-bottom-8"][{number}]/div/div/span/div/span[2]'
        FIELD_TITLES: str = f'//div[@class="flex-column flex-grow kanban-board-column padding-bottom-8"][{number}]/div/div/span/div/a/span'
        FIELD_EFFORT: str = f'//div[@class="flex-column flex-grow kanban-board-column padding-bottom-8"][{number}]/div/div[2]/div/div[2]/div/div[2]/div'
        return (FIELD_NUMBERS, FIELD_TITLES, FIELD_EFFORT)


backlogs_states: list[str] = [
    'New',
    'Approved',
    'Committed',
    'External',
    'Test',
    'Accepted',
    'Review',
    'Done',
]

APPROVEDS_COMMENTS: list[str] = [
    'pre:aprovada',
    'pre:aprovado',
    'pré:aprovado',
    'pré:aprovada',
    'prod:aprovado',
    'prod:aprovada',
]

COMMENTS: str = "//div[@class='comment-item flex-row displayed-comment depth-8 markdown-discussion-comment']/div[2]/div/div[2]"
FEATURES: str = "//div[@class='artifact-link-id secondary-text margin-right-4']"

SUSTENTACAO: str = 'Sustentação - |Sustentação-|Sustentação -|Sustentação- |sustentação - |sustentação-|sustentação -|sustentação- |sustentacao - |sustentacao-|sustentacao- |sustentacao -|sustentacão - |sustentacao-|sustentacao- |sustentacao -|- Q1|- Q2|- Q3|-Q1|-Q2|-Q3| Q1|Q 1|Q - 1|Q-1|Q -1|Q-|q1|q 1|q - 1|q-1|q -1| Q1| Q 1| Q - 1| Q-1| Q -1| Q- 1| q1| q 1| q - 1| q-1| q -1|____|Q2|Q 2|Q - 2|Q-2|Q -2|Q- 2|q2|q 2|q - 2|q-2|q -2| Q2| Q 2| Q - 2| Q-2| Q -2| Q- 2| q2| q 2| q - 2| q-2| q -2|____|Q3|Q 3|Q - 3|Q-3|Q -3|Q- 3|q3|q 3|q - 3|q-3|q -3| Q3| Q 3| Q - 3| Q-3| Q -3| Q- 3| q3| q 3| q - 3| q-3| q -3|'

SUST_REGEX = compile(
    r"""^(
        (sustenta[cç][aã]o\s*-\s*)|                         # Sustentação com variações de acento e espaço/hífen
        (-\s*Q[1-3])|                                       # -Q1, - Q2 etc.
        (Q\s*-\s*[1-3])|                                    # Q - 1 etc.
        (Q\s*[1-3])|                                        # Q1, Q 2 etc.
        (q\s*-\s*[1-3])|                                    # q - 1 etc.
        (q\s*[1-3])|                                        # q1, q 3 etc.
        (Q-\s*[1-3])|                                       # Q- 2 etc.
        (q-\s*[1-3])|                                       # q- 3 etc.
        (____)                                              # underline literal
    )$""",
    IGNORECASE | VERBOSE,
)
