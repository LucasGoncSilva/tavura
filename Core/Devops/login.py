from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from Core.Devops import constants
from time import sleep

class Login():
    
    @classmethod
    def authenticate(cls):
        cls.options = webdriver.ChromeOptions()
        # cls.options.add_argument("-headless")
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.mail: str = constants.MAIL
        cls.password: str = constants.PASS

        # Iniciando a sessão
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://dev.azure.com/ONR-SAEC/ONR.Sustentacao/_boards/board/t/ONR.Sustentacao%20Team/Backlog%20items?System.AreaPath=ONR.Sustentacao')
        cls.driver.maximize_window()

        mail_field: WebDriver = cls.driver.find_element(
            By.XPATH, "//input[@type='email']"
        )
        mail_field.send_keys(cls.mail)
        mail_field.send_keys(Keys.ENTER)

        pass_field: WebDriver = cls.driver.find_element(
            By.XPATH, "//input[@type='password']"
        )
        pass_field.send_keys(cls.password)

        btn_entrar: WebDriver = cls.driver.find_element(
            By.XPATH, "//input[@value='Entrar']"
        )
        btn_entrar.click()

        stay_connected: WebDriver = cls.driver.find_element(
            By.XPATH, "//input[@type='submit']"
        )
        stay_connected.click()

        sleep(5)
    
    @classmethod
    def shut_down(cls, driver):
        driver.quit()
