from app.system.constants import Constants
from selenium.webdriver.common.by import By
from app.system import constants
from time import sleep
from app.auth.login import Login


class GetBacklogs(Login):
    @classmethod
    def get_backlogs(cls, states: str) -> dict:
        backlogs: list[dict]
        backlogs_element: list

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
            if state in _states and state in states_mapings.keys(): #Desnecessary state in states_mapings.keys()
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
                    backlogs_element.extend(numbers)
                except:
                    backlogs_element.extend("")
                    print(f"PBIs of the state: {state} it's null")

                for number, title, effort in zip(numbers, titles, efforts):
                    _effort = effort.text.replace("Effort\n", "")
                    if _effort.isnumeric():
                        backlogs.append(
                            {
                                "PBI": number.text,
                                "DESCRIÇÃO": title.text,
                                "STATUS": " ",
                                "EFFORT": _effort,
                                "FEATURE": "NÃO",
                            }
                        )
                    else:
                        backlogs.append(
                            {
                                "PBI": number.text,
                                "DESCRIÇÃO": title.text,
                                "STATUS": " ",
                                "EFFORT": "N/A",
                                "FEATURE": "NÃO",
                            }
                        )
        encapsuled: list = []
        encapsuled.append((backlogs, backlogs_element))
        return encapsuled
    
    @classmethod
    def get_pbi(cls, number) -> dict | None:
        pbi = next((pbi for pbi in cls.backlogs if pbi["PBI"] == number), None)
        return pbi