from os import remove
from os.path import exists

from pandas import DataFrame
from selenium.webdriver.remote.webelement import WebElement


class Excel:
    OUTPUT: str = 'Relatório de PBI.xlsx'

    @classmethod
    def get_relatorio(cls, backlogs: list[dict[str, str | WebElement]]) -> None:
        planilha: DataFrame = DataFrame(data=backlogs)
        planilha.to_excel(cls.OUTPUT, index=False)  # type: ignore

    @classmethod
    def remove_xls(cls) -> None:
        if exists(cls.OUTPUT):
            try:
                remove(cls.OUTPUT)
            except Exception as e:
                print(f'An error ocurred: {str(e)}')
