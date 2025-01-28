from app.system import constants
import re

class Treatment():
    @classmethod
    def remove_garbage(cls, backlogs) -> dict:
        backlog_: list[dict]
        sustentacao = constants.SUSTENTACAO
        for backlog in backlogs:
            description: str = re.sub(sustentacao, "", backlog["DESCRIÇÃO"])
            backlog_.update({"DESCRIÇÃO": description})

        return backlog_

    def ordenate(cls, backlogs) -> list[dict]:
        return sorted(backlogs) #Develop