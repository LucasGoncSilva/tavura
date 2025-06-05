from os import remove
from os.path import exists
from typing import Self

from pandas import DataFrame
from selenium.webdriver.remote.webelement import WebElement


class Excel:
    OUTPUT: str = 'Relatório de PBI.xlsx'

    @classmethod
    def get_relatorio(
        cls: type[Self], backlogs: list[dict[str, str | WebElement]]
    ) -> None:
        """
        Creates the final report.

        Using `pandas.to_excel`, saves the recieved `backlogs` after `pandas.DataFrame`
        converts it to a df.

        :param backlogs: Default struct of PBIs group to be clear.
        :type backlogs: list[dict[str, str | WebElement]]
        :returns: None.
        :rtype: None
        :raises: None
        """

        planilha: DataFrame = DataFrame(data=backlogs)
        planilha.to_excel(cls.OUTPUT, index=False)  # type: ignore

    @classmethod
    def remove_xls(cls: type[Self]) -> None:
        """
        Deletes the old report, if exists.

        Just check for any existing xlsx report with the expected name and try to delete
        it, raising an exception that has never been raised before.

        :returns: None.
        :rtype: None
        :raises: NotImplementedError
        """

        if exists(cls.OUTPUT):
            try:
                remove(cls.OUTPUT)
            except Exception as e:
                raise NotImplementedError(f'An error ocurred: {str(e)}')
