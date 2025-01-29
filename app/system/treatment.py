from app.system import constants
import re

class Treatment():
    @classmethod
    def remove_garbage(cls, backlogs) -> dict:
        backlogs_: list[dict] = backlogs
        sustentacao = constants.SUSTENTACAO
        for backlog in backlogs_:
            description: str = re.sub(sustentacao, "", backlog["DESCRIÇÃO"])
            backlog.update({"DESCRIÇÃO": description})

        print(backlogs_)
        return backlogs_

    def ordenate(cls, backlogs) -> list[dict]:
        return sorted(backlogs) #Develop