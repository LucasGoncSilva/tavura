from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Chrome, ChromeOptions, Edge, EdgeOptions, Firefox, FirefoxOptions
 

class Browser():
    @classmethod
    def link_browser(cls, browser):
        browsers: dict = {
            'Chrome': (Chrome, ChromeOptions),
            'Firefox': (Firefox, FirefoxOptions),
            'Edge': (Edge, EdgeOptions),
        }

        options = browsers[browser][1]()
        # options.add_argument("-headless")
 
        cls.driver: WebDriver = browsers[browser][0](options)
        cls.driver.get('https://dev.azure.com/ONR-SAEC/ONR.Sustentacao/_boards/board/t/ONR.Sustentacao%20Team/Backlog%20items?System.AreaPath=ONR.Sustentacao')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def shut_down(cls, driver):
        driver.quit()