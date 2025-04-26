from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.drivers.browser import Browser


class Login(Browser):
    @classmethod
    def authenticate(cls, mail_, pass_):
        # Firefox | Edge | Chrome
        cls.link_browser('Edge')

        mail_field: WebElement = cls.driver.find_element(
            By.XPATH, "//input[@type='email']"
        )
        mail_field.send_keys(mail_)
        mail_field.send_keys(Keys.ENTER)

        pass_field: WebElement = cls.driver.find_element(
            By.XPATH, "//input[@type='password']"
        )
        pass_field.send_keys(pass_)
    
        WebDriverWait(cls.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "inline-block button-item ext-button-item")
        ))

        btn_access = WebDriverWait(cls.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))
        )
        btn_access.click()

        stay_connected: WebElement = cls.driver.find_element(
            By.XPATH, "//input[@type='submit']"
        )
        stay_connected.click()

    @classmethod
    def quit_driver(cls):
        cls.driver.quit()
