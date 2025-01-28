from app import constants
import re

class Treatment():
    @classmethod
    def remove_garbage(cls, backlogs) -> None:
        sustentacao = constants.SUSTENTACAO
        for backlog in backlogs:
            description: str = re.sub(sustentacao, "", backlog["DESCRIÇÃO"])
            backlog.update({"DESCRIÇÃO": description})

    def ordenate(cls, backlogs) -> list[dict]:
        return sorted(backlogs) #Develop