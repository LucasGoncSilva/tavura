from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.auth.login import Login
from app.system import constants
from app.system.constants import Constants


class GetBacklogs(Login):
    numbers = []
    titles = []
    efforts = []

    @classmethod
    def get_backlogs(cls, states: str | None) -> list[dict[str, str | WebElement]]:
        backlogs: list[dict[str, str]] = []
        backlogs_element: list[WebElement] = []

        if states is None:
            raise TypeError("Expected 'STATUS' to be localized PBIs but found NoneType")

        _states: list[str] = states.split(' ')

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
        for state in constants.backlogs_states:
            if state in _states and state in states_mapings.keys():
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
                    _effort = effort.text.replace('Effort\n', '')
                    if _effort.isnumeric():
                        backlogs.append(
                            {
                                'PBI': number.text,
                                'DESCRIÇÃO': title.text,
                                'STATUS': ' ',
                                'EFFORT': _effort,
                                'FEATURE': 'NÃO',
                            }
                        )
                    else:
                        backlogs.append(
                            {
                                'PBI': number.text,
                                'DESCRIÇÃO': title.text,
                                'STATUS': ' ',
                                'EFFORT': 'N/A',
                                'FEATURE': 'NÃO',
                            }
                        )
        encapsuled: list[dict[str, str] | WebElement] = []
        encapsuled.append(backlogs)
        encapsuled.append(backlogs_element)
        return encapsuled

    @classmethod
    def get_pbi(cls, number) -> dict | None:
        pbi = next((pbi for pbi in cls.backlogs if pbi['PBI'] == number), None)
        return pbi
