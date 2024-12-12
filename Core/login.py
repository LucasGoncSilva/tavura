from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from Core.browser import Browser
from Core import constants


class Login(Browser):
    @classmethod
    def authenticate(cls):
        cls.mail: str = constants.MAIL # type: ignore
        cls.password: str = constants.PASS # type: ignore

        cls.link_browser('Chrome')

        mail_field: WebElement = cls.driver.find_element(
            By.XPATH, "//input[@type='email']"
        )
        mail_field.send_keys(cls.mail)
        mail_field.send_keys(Keys.ENTER)

        pass_field: WebElement = cls.driver.find_element(
            By.XPATH, "//input[@type='password']"
        )
        pass_field.send_keys(cls.password)

        btn_entrar: WebElement = cls.driver.find_element(
            By.XPATH, "//input[@value='Entrar']"
        )
        btn_entrar.click()

        stay_connected: WebElement = cls.driver.find_element(
            By.XPATH, "//input[@type='submit']"
        )
        stay_connected.click()
