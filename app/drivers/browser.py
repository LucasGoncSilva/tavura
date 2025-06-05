from os import getenv
from typing import Literal, Self

from selenium.webdriver import (
    Chrome,
    ChromeOptions,
    Edge,
    EdgeOptions,
    Firefox,
    FirefoxOptions,
)
from selenium.webdriver.remote.webdriver import WebDriver


Drivers = type[Chrome | Firefox | Edge]
DriversOpt = type[ChromeOptions | FirefoxOptions | EdgeOptions]


class Browser:
    @classmethod
    def link_browser(
        cls: type[Self], browser: Literal['Chrome', 'Firefox', 'Edge']
    ) -> None:
        """
        Defines the Browser to be used.

        By receiving an option of Chrome, Firefox or Edge, this function instanciates
        one of them with the appropriated Option class, setting headless or not,
        implicit wait default time as 10 seconds and GET the first URL.

        :param browser: The browser to be used.
        :type browser: Literal['Chrome', 'Firefox', 'Edge']
        :returns: None.
        :rtype: None
        :raises: None
        """

        browsers: dict[str, tuple[Drivers, DriversOpt]] = {
            'Chrome': (Chrome, ChromeOptions),
            'Firefox': (Firefox, FirefoxOptions),
            'Edge': (Edge, EdgeOptions),
        }

        options = browsers[browser][1]()
        if getenv('HEADLESS'):
            options.add_argument('-headless')  # type: ignore

        cls.driver: WebDriver = browsers[browser][0](options)  # type: ignore
        cls.driver.get(
            'https://dev.azure.com/ONR-SAEC/ONR.Sustentacao/_boards/board/t/ONR.Sustentacao%20Team/Backlog%20items?System.AreaPath=ONR.Sustentacao'
        )
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
