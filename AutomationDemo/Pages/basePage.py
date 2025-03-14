from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from AutomationDemo.utils import driverFactory


class BasePage:

    def __init__(self,driver=None):
        self.driver = driver if driver else driverFactory.WebDriverManager.get_driver()

    def open_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver,timeout=10).until(expected_conditions.presence_of_element_located(locator))

    def click_element(self, locator_type,locator_value):
        element = self.driver.find_element(locator_type,locator_value)
        element.click()

    def enter_text(self,locator_type,locator_value):
        text = self.driver.find_element(locator_type,locator_value)
        text.clear()
        text.send_keys("Test data")

    def find_elements(self,locator_type,locator_value) :
        webelements = self.driver.find_elements(locator_type,locator_value)
        return webelements


