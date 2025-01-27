from core.constants import Constants
from core import constants
from time import sleep


class GetBacklogs():
    @classmethod
    def getBacklogs(cls, states: str) -> None:
        if states is None:
            raise TypeError("Expected 'STATUS' to be localized PBIs but found NoneType")
        
        _states: list[str] = states.split(" ")
         
        states_mapings: dict = {
            "New": (Constants.get_fields(1)),
            "Approved": (Constants.get_fields(2)),
            "Committed": (Constants.get_fields(3)),
            "External": (Constants.get_fields(4),),
            "Test": (Constants.get_fields(5)),
            "Accepted": (Constants.get_fields(6)),
            "Review": (Constants.get_fields(7)),
            "Done": (Constants.get_fields(8)),
        }

        """Necessary sleep to work"""
        sleep(3) 
        for state in constants.backlogs_states:
            if state in states and state in states_mapings.keys():
                try:
                    cls.driver.implicitly_wait(2)
                    numbers = cls.driver.find_elements(
                        By.XPATH, states_mapings[state][0]
                    )
                    titles = cls.driver.find_elements(
                        By.XPATH, states_mapings[state][1]
                    )
                    efforts = cls.driver.find_elements(
                        By.XPATH, states_mapings[state][2]
                    )
                    cls.backlogs_element.extend(numbers)
                except:
                    cls.backlogs_element.extend("")
                    print(f"PBIs of the state: {state} it's null")