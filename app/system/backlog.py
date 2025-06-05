from logging import Logger, getLogger
from time import sleep
from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.auth.login import Login
from app.system import constants
from app.system.constants import Constants


logger: Logger = getLogger('tavura')


class GetBacklogs(Login):
    numbers: list[WebElement] = []
    titles: list[WebElement] = []
    efforts: list[WebElement] = []

    @classmethod
    def get_backlogs(
        cls: type[Self], states: list[str] | None
    ) -> list[list[dict[str, str]] | list[WebElement | str]]:
        """
        Gets product backlog items based on provided `states`.

        Gets and returns a matrix containing every found PBI with same state as the
        expected ones, with their title, effort and last comment

        :param states: PBIs states to be tracked
        :type states: list[str] | None
        :returns: Matrix of backlogs
        :rtype: list[list[dict[str, str]] | list[WebElement | str]]
        :raises: TypeError
        """

        backlogs: list[dict[str, str]] = []
        backlogs_element: list[WebElement | str] = []

        if states is None:
            raise TypeError("Expected 'STATUS' to be localized PBIs but found NoneType")

        states_mapings: dict[str, tuple[str, str, str]] = {
            'New': Constants.get_fields(0),
            'Approved': Constants.get_fields(1),
            'Committed': Constants.get_fields(2),
            'External': Constants.get_fields(3),
            'Test': Constants.get_fields(4),
            'Accepted': Constants.get_fields(5),
            'Review': Constants.get_fields(6),
            'Done': Constants.get_fields(7),
        }

        """Necessary sleep to work"""
        sleep(5)
        for state in constants.BACKLOGS_STATES:
            if state in states and state in states_mapings.keys():
                logger.info(f'Iterating {state} PBIs')
                try:
                    cls.driver.implicitly_wait(2)
                    cls.numbers = cls.driver.find_elements(
                        By.XPATH, states_mapings[state][0]
                    )
                    cls.titles = cls.driver.find_elements(
                        By.XPATH, states_mapings[state][1]
                    )
                    cls.efforts = cls.driver.find_elements(
                        By.XPATH, states_mapings[state][2]
                    )
                    backlogs_element.extend(cls.titles)
                except Exception:
                    backlogs_element.extend('')
                    print(f"PBIs of the state: {state} it's null")

                for number, title, effort in zip(cls.numbers, cls.titles, cls.efforts):
                    logger.debug(f'Adding PBI: {number.text}')

                    _effort = effort.text.replace('Effort\n', '')

                    if _effort.isnumeric():
                        backlogs.append(
                            {
                                'PBI': number.text,
                                'DESCRIÇÃO': title.text,
                                'STATUS': 'NotImplementedError',
                                'EFFORT': _effort,
                                'FEATURE': 'NÃO',
                            }
                        )
                    else:
                        backlogs.append(
                            {
                                'PBI': number.text,
                                'DESCRIÇÃO': title.text,
                                'STATUS': 'NotImplementedError',
                                'EFFORT': 'N/A',
                                'FEATURE': 'NÃO',
                            }
                        )

        encapsuled: list[list[dict[str, str]] | list[WebElement | str]] = []
        encapsuled.append(backlogs)
        encapsuled.append(backlogs_element)
        return encapsuled
