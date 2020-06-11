from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self, url):
        return self.driver.get(url)

    def out(self):
        return self.driver.quit()

    def find_and_click(self, locator):
        element = self.find_element(locator)
        element.click()
