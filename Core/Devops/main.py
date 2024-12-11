import re
import time
import os
from os import environ as env

import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from Core.Devops import constants
from Core.Devops.constants import Constants
from Core.Devops.login import Login


class Main(Login):
    backlogs: list = []
    backlogs_element: list = []
    numbers: list = []
    numbers_ordened: list = []
    title: list = []
    effort: list = []
    comments: list[WebElement] = [] 

    @classmethod
    def main(cls):
        start: float = time.time()
        cls.remove_xlsx()
        cls.authenticate()
        cls.get_backlogs()
        cls.check_backlogs()
        cls.remove_garbage()
        cls.shut_down(cls.driver)
        cls.get_relatorio()
        end: float = time.time()
        print(f"Duration of the program: '{end - start:.2f}s'")

    @classmethod
    def get_backlogs(cls) -> None:
        _states: str = str(env.get("state"))
        if _states is None:
            raise TypeError("Expected 'STATUS' to be localized PBIs but found NoneType")


        states: list[str] = _states.split(" ")
        print(states)
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

        time.sleep(3)
        for state in backlogs_states:
            if state in states and state in states_mapings.keys():
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
                    # print(cls.numbers.text)
                    cls.backlogs_element.extend(cls.numbers)
                except:
                    cls.backlogs_element.extend("")
                    print(f"PBIs of the state: {state} it's null")

                for number, title, effort in zip(cls.numbers_ordened, cls.titles, cls.efforts):
                    _effort = effort.text.replace("Effort\n", "")
                    if _effort.isnumeric():
                        cls.backlogs.append(
                            {
                                "PBI": number,
                                "DESCRIÇÃO": title.text,
                                "STATUS": " ",
                                "EFFORT": _effort,
                                "FEATURE": "NÃO",
                            }
                        )
                    else:
                        cls.backlogs.append(
                            {
                                "PBI": number,
                                "DESCRIÇÃO": title.text,
                                "STATUS": " ",
                                "EFFORT": "N/A",
                                "FEATURE": "NÃO",
                            }
                        )

    @classmethod
    def remove_garbage(cls) -> None:
        sustentacao = constants.SUSTENTACAO
        for backlog in cls.backlogs:
            description: str = re.sub(sustentacao, "", backlog["DESCRIÇÃO"])
            backlog.update({"DESCRIÇÃO": description})

    @classmethod
    def check_backlogs(cls) -> None:
        approved_comments: list[str] = str(env.get("approveds_comments")).split()

        for backlog in cls.backlogs_element:
            cls.driver.implicitly_wait(.3)
            action = ActionChains(cls.driver)
            action.move_to_element(backlog).click().perform()
            # New future implementation
            # url = constants.URL + backlog.text
            # cls.driver.get(url)

            try:
                cls.comments: list[WebElement] = cls.driver.find_elements(
                    By.XPATH, constants.COMMENTS
                )
            except Exception as e:
                print(f"An error ocurred: {str(e)}")

            try:
                feature: WebElement | str = cls.driver.find_element(
                    By.XPATH, constants.FEATURES
                )
            except:
                feature: WebElement | str = " "

            if feature != " ":
                if "11119" in feature.text:
                    pbi = cls.find_pbi(backlog.text)
                    if pbi:
                        pbi.update({"FEATURE": "SIM"})

            for approved in approved_comments:
                """Obtenção da PBI e adiciona OK em status"""
                if any(
                    approved in comment.text.lower().replace(" ", "")
                    for comment in cls.comments
                ):
                    pbi = cls.find_pbi(backlog.text)
                    if pbi:
                        if "pre" in approved:
                            pbi.update({"STATUS": "PRE: OK"})
                        elif "prod" in approved:
                            pbi.update({"STATUS": "PROD: OK"})
            cls.driver.back()

    @classmethod
    def find_pbi(cls, number) -> dict | None:
        pbi = next((pbi for pbi in cls.backlogs if pbi["PBI"] == number), None)
        return pbi

    @classmethod
    def get_relatorio(cls) -> None:
        planilha = pd.DataFrame(data=sorted(cls.backlogs))
        planilha.to_excel("Relatório de PBI.xlsx", index=False)

    @classmethod
    def remove_xlsx(cls) -> None:
        rel: str = "Relatório de PBI.xlsx"
        if os.path.exists(rel):
            try:
                os.remove(rel)
            except Exception as e:
                print(f"An error ocurred: {str(e)}")
