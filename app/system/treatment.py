from logging import Logger, getLogger
from re import sub
from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from app.system.constants import SUSTENTACAO


logger: Logger = getLogger('tavura')


class Treatment:
    @classmethod
    def remove_garbage(
        cls: type[Self], backlogs: list[dict[str, str | WebElement]]
    ) -> list[dict[str, str | WebElement]]:
        """
        Removes unnecessary standard content from the last comment of a PBI.

        By applying a `re.sub` using the args `app.system.constants.SUSTENTACAO` and
        the description (comment) itself, updates any found match to empty text `''`.

        :param backlogs: Default struct of PBIs group to be clear.
        :type backlogs: list[dict[str, str | WebElement]]
        :returns: The same default struct of PBIs, sanitized.
        :rtype: list[dict[str, str | WebElement]]
        :raises: None
        """

        logger.info("Sanitizing backlogs's last comments")
        for backlog in backlogs:
            logger.debug(f'Sanitizing {backlog["PBI"]}')
            backlog['DESCRIÇÃO'] = sub(SUSTENTACAO, '', backlog['DESCRIÇÃO'])  # type: ignore

        new_backlogs: list[dict[str, str | WebElement]] = backlogs.copy()
        return new_backlogs
