from typing import Self
from typing import Final
from os import getenv
from re import compile, IGNORECASE, VERBOSE
from dotenv import load_dotenv


load_dotenv()

MAIL: str | None = getenv('MAIL')
PASS: str | None = getenv('PASS')


if any(map(lambda x: x is None, [MAIL, PASS])):
    raise TypeError(
        f'Expected "MAIL" and "PASS" to be string, got "{type(MAIL)}", "{type(PASS)}"'
    )


class Constants:
    DEFAULT_PATH: Final[str] = (
        '//div[@class="flex-column flex-grow kanban-board-column padding-bottom-8"]'
    )

    @classmethod
    def get_fields(cls: type[Self], number: int) -> tuple[str, str, str]:
        """
        Returns the constant XPATH for core PBIs infos.

        By handling default XPATH values and filling the designed space for the diven
        number - using f-string - formats the constant XPATH and returns a tuple.

        :param number: XPATH ordinary number for a given PBI
        :type number: int
        :returns: A tuple with the XPATH for the number, title and effort.
        :rtype: tuple[str, str, str]
        :raises: None
        """

        FIELD_NUMBERS: Final[str] = '/div/div/span/div/span[2]'
        FIELD_TITLES: Final[str] = '/div/div/span/div/a/span'
        FIELD_EFFORT: Final[str] = '/div/div[2]/div/div[2]/div/div[2]/div'

        return (
            cls.DEFAULT_PATH + f'[{number}]' + FIELD_NUMBERS,
            cls.DEFAULT_PATH + f'[{number}]' + FIELD_TITLES,
            cls.DEFAULT_PATH + f'[{number}]' + FIELD_EFFORT,
        )


BACKLOGS_STATES: Final[list[str]] = [
    'New',
    'Approved',
    'Committed',
    'External',
    'Test',
    'Accepted',
    'Review',
    'Done',
]

APPROVEDS_COMMENTS: Final[list[str]] = [
    'pre:aprovada',
    'pre:aprovado',
    'pré:aprovado',
    'pré:aprovada',
    'prod:aprovado',
    'prod:aprovada',
]

COMMENTS: Final[str] = (
    "//div[@class='comment-item flex-row displayed-comment depth-8 markdown-discussion-comment']/div[2]/div/div[2]"
)
FEATURES: Final[str] = "//div[@class='artifact-link-id secondary-text margin-right-4']"

SUSTENTACAO: Final[str] = (
    'Sustentação - |Sustentação-|Sustentação -|Sustentação- |sustentação - |sustentação-|sustentação -|sustentação- |sustentacao - |sustentacao-|sustentacao- |sustentacao -|sustentacão - |sustentacao-|sustentacao- |sustentacao -|- Q1|- Q2|- Q3|-Q1|-Q2|-Q3| Q1|Q 1|Q - 1|Q-1|Q -1|Q-|q1|q 1|q - 1|q-1|q -1| Q1| Q 1| Q - 1| Q-1| Q -1| Q- 1| q1| q 1| q - 1| q-1| q -1|____|Q2|Q 2|Q - 2|Q-2|Q -2|Q- 2|q2|q 2|q - 2|q-2|q -2| Q2| Q 2| Q - 2| Q-2| Q -2| Q- 2| q2| q 2| q - 2| q-2| q -2|____|Q3|Q 3|Q - 3|Q-3|Q -3|Q- 3|q3|q 3|q - 3|q-3|q -3| Q3| Q 3| Q - 3| Q-3| Q -3| Q- 3| q3| q 3| q - 3| q-3| q -3|'
)

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
