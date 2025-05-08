from re import sub

from selenium.webdriver.remote.webelement import WebElement

from app.system.constants import SUSTENTACAO


class Treatment:
    @classmethod
    def remove_garbage(
        cls, backlogs: list[dict[str, str | WebElement]]
    ) -> list[dict[str, str | WebElement]]:
        new_backlogs: list[dict[str, str | WebElement]]
        for backlog in backlogs:
            description: str = sub(SUSTENTACAO, '', backlog['DESCRIÇÃO'])
            backlog.update({'DESCRIÇÃO': description})

        new_backlogs = backlogs.copy()
        return new_backlogs
