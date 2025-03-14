from selenium.webdriver.common.by import By
from AutomationDemo.Pages.basePage import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self,url):
        self.open_url(url)

    def enter_username(self,locator_type,locator_value):
        self.enter_text(locator_type,locator_value)

    def enter_password(self,locator_type,locator_value):
        self.enter_text(locator_type,locator_value)

    def click(self,locator_type,locator_value):
        self.click_element(locator_type,locator_value)

