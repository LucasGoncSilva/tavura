import pandas as pd
import os


class Excel():
    @classmethod
    def get_relatorio(cls, backlogs) -> None:
        planilha = pd.DataFrame(data=backlogs)
        planilha.to_excel("Relatório de PBI.xlsx", index=False)

    @classmethod
    def remove_xls(cls) -> None:
        rel: str = "Relatório de PBI.xlsx"
        if os.path.exists(rel):
            try:
                os.remove(rel)
            except Exception as e:
                print(f"An error ocurred: {str(e)}")