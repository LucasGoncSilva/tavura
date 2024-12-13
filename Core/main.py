import re
import time
import os
import pandas as pd
from tkinter import *
from tqdm import tqdm
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Core import constants
from Core.constants import Constants
from Core.login import Login



class Main(Login):
    backlogs: list = []
    backlogs_element: list = []
    comments: list[WebElement] = [] 

    @classmethod
    def main(cls, mail_, pass_, checks):
        start_time = time.time()
        cls.mail_ = mail_
        cls.pass_ = pass_
        cls.states = " "
        

        for chave, item in checks.items():
            if item == True:
                cls.states += chave + " "

        try:
            cls.run_pipeline()
        finally:
            cls.report_duration(start_time)
            return cls.backlogs
        

    @classmethod
    def run_pipeline(cls):
        cls.remove_xls()
        cls.authenticate(cls.mail_, cls.pass_)
        cls.get_backlogs(cls.states)
        cls.validate_backlogs()
        cls.remove_garbage()
        cls.shut_down()
        cls.get_relatorio()

    @classmethod
    def report_duration(cls, start_time: float):
        end_time = time.time()
        duration = end_time - start_time
        print(f"Duration of the program: {duration:.2f}s")

    @classmethod
    def get_backlogs(cls, _states) -> None:
        if _states is None:
            raise TypeError("Expected 'STATUS' to be localized PBIs but found NoneType")

        states: list[str] = _states.split(" ")

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


        numbers: list[WebElement] = []
        titles: list[WebElement] = []
        efforts: list[WebElement] = []
        
        """Necessary sleep to work"""
        time.sleep(3)
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

                for number, title, effort in zip(numbers, titles, efforts):
                    _effort = effort.text.replace("Effort\n", "")
                    if _effort.isnumeric():
                        cls.backlogs.append(
                            {
                                "PBI": number.text,
                                "DESCRIÇÃO": title.text,
                                "STATUS": " ",
                                "EFFORT": _effort,
                                "FEATURE": "NÃO",
                            }
                        )
                    else:
                        cls.backlogs.append(
                            {
                                "PBI": number.text,
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
    def validate_backlogs(cls) -> None:
        approved_comments: list[str] = str(constants.APPROVEDS_COMMENTS).split()

        for backlog in tqdm(cls.backlogs_element):
            cls.driver.implicitly_wait(.3)
            action = ActionChains(cls.driver)
            action.move_to_element(backlog).click().perform()

            try:
                cls.comments: list[WebElement] = cls.driver.find_elements(
                    By.XPATH, constants.COMMENTS
                )
            except Exception as e:
                print(f"An error ocurred: {str(e)}")

            try:
                feature = cls.driver.find_element(
                    By.XPATH, constants.FEATURES
                )
            except:
                feature = " "

            if feature != " ":
                if "11119" in feature.text: # type: ignore
                    pbi = cls.get_pbi(backlog.text)
                    if pbi:
                        pbi.update({"FEATURE": "SIM"})

            for approved in approved_comments:
                """Obtenção da PBI e adiciona OK em status"""
                if any(
                    approved in comment.text.lower().replace(" ", "")
                    for comment in cls.comments
                ):
                    pbi = cls.get_pbi(backlog.text)
                    if pbi:
                        if "pre" in approved:
                            pbi.update({"STATUS": "PRE: OK"})
                        elif "prod" in approved:
                            pbi.update({"STATUS": "PROD: OK"})
            cls.driver.back()

    @classmethod
    def get_pbi(cls, number) -> dict | None:
        pbi = next((pbi for pbi in cls.backlogs if pbi["PBI"] == number), None)
        return pbi

    @classmethod
    def get_relatorio(cls) -> None:
        planilha = pd.DataFrame(data=cls.backlogs)
        planilha.to_excel("Relatório de PBI.xlsx", index=False)

    @classmethod
    def remove_xls(cls) -> None:
        rel: str = "Relatório de PBI.xlsx"
        if os.path.exists(rel):
            try:
                os.remove(rel)
            except Exception as e:
                print(f"An error ocurred: {str(e)}")

    
    @classmethod
    def shut_down(cls):
        cls.driver.quit()
