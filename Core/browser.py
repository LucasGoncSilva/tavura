from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Chrome, ChromeOptions, Edge, EdgeOptions, Firefox, FirefoxOptions
from time import sleep
 

class Browser():
    @classmethod
    def link_browser(cls, browser, counter):
        browsers: dict = {
            'Chrome': (Chrome, ChromeOptions),
            'Firefox': (Firefox, FirefoxOptions),
            'Edge': (Edge, EdgeOptions),
        }

        print(counter)
        options = browsers[browser][1]()
        # options.add_argument("-headless")
        porta = 9222 + counter
        porta = str(porta)
        options.add_argument(f'--remote-debugging-port={porta}')
 
        cls.driver: WebDriver = browsers[browser][0](options)
        cls.driver.get('https://dev.azure.com/ONR-SAEC/ONR.Sustentacao/_boards/board/t/ONR.Sustentacao%20Team/Backlog%20items?System.AreaPath=ONR.Sustentacao')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

