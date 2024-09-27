import re
import time
import os
from os import environ as env

import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from Core.Devops import constants
from Core.Devops.login import Login


class Main(Login):
    backlogs: list = []
    backlogs_element: list = []

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
        backlogs_states: list = [
            "New",
            "Approved",
            "Committed",
            "Test",
            "Accepted",
            "Review",
            "Done",
        ]

        states_mapings: dict = {
            "New": (constants.NEW_NUMBERS, constants.NEW_TITLES, constants.NEW_EFFORT),
            "Approved": (
                constants.APPROVED_NUMBERS,
                constants.NEW_TITLES,
                constants.APPROVED_EFFORT,
            ),
            "Committed": (
                constants.COMMITTED_NUMBERS,
                constants.COMMITTED_TITLES,
                constants.COMMITTED_EFFORT,
            ),
            "Test": (
                constants.TEST_NUMBERS,
                constants.TEST_TITLES,
                constants.TEST_EFFORT,
            ),
            "Accepted": (
                constants.ACCEPTED_NUMBERS,
                constants.ACCEPTED_TITLES,
                constants.ACCEPTED_EFFORT,
            ),
            "Review": (
                constants.REVIEW_NUMBERS,
                constants.REVIEW_TITLES,
                constants.REVIEW_TITLES,
            ),
            "Done": (
                constants.DONE_NUMBERS,
                constants.DONE_TITLES,
                constants.DONE_EFFORT,
            ),
        }

        for state in backlogs_states:
            if state in states and state in states_mapings.keys():
                numbers: list[WebElement] = cls.driver.find_elements(
                    By.XPATH, states_mapings[state][0]
                )
                titles: list[WebElement] = cls.driver.find_elements(
                    By.XPATH, states_mapings[state][1]
                )
                efforts: list[WebElement] = cls.driver.find_elements(
                    By.XPATH, states_mapings[state][2]
                )

                cls.backlogs_element.extend(numbers)

                for number, title, effort in zip(numbers, titles, efforts):
                    cls.backlogs.append(
                        {
                            "PBI": number.text,
                            "DESCRIÇÃO": title.text,
                            "STATUS": "",
                            "EFFORT": effort.text.replace("Effort\n", ""),
                            "FEATURE": "NÃO",
                        }
                    )

    @classmethod
    def remove_garbage(cls):
        sustentacao = constants.SUSTENTACAO
        for backlog in cls.backlogs:
            description: str = re.sub(sustentacao, "", backlog["DESCRIÇÃO"])
            backlog.update({"DESCRIÇÃO": description})

    @classmethod
    def check_backlogs(cls) -> None:
        approved_comments: list[str] = str(env.get("approveds_comments")).split()

        for backlog in cls.backlogs_element:
            action = ActionChains(cls.driver)
            action.move_to_element(backlog).click().perform()

            try:
                comments: list[WebElement] = cls.driver.find_elements(
                    By.XPATH, constants.COMMENTS
                )
            except Exception as e:
                print(f"An error ocurred: {str(e)}")

            try:
                feature: WebElement | str = cls.driver.find_element(
                    By.XPATH, constants.FEATURES
                )
            except Exception as e:
                print(f"An error ocurred: {str(e)}")
                feature: WebElement | str = ""

            # if isinstance(feature, WebElement):
            if feature != "":
                if "11119" in feature.text:
                    pbi = cls.find_pbi(backlog.text)
                    if pbi:
                        pbi.update({"FEATURE": "SIM"})

            for approved in approved_comments:
                """Obtenção da PBI e adiciona OK em status"""
                if any(
                    approved in comment.text.lower().replace(" ", "")
                    for comment in comments
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
    def get_relatorio(cls):
        planilha = pd.DataFrame(data=cls.backlogs)
        planilha.to_excel("Relatório de PBI.xlsx", index=False)

    @classmethod
    def remove_xlsx(cls):
        try:
            os.remove("Relatório de PBI.xlsx")
        except:
            ...
