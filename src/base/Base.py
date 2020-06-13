from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(expected_conditions.presence_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")

    def go_to_site(self, url):
        self.driver.get(url)

    def find_and_click(self, locator, timer=0.1):
        element = self.find_element(locator)
        element.click()
        #Ожидание после нажатия (если необходимо)
        time.sleep(timer)
