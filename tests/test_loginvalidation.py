from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from AutomationDemo.Pages.loginPage import LoginPage
from AutomationDemo.utils.driverFactory import WebDriverManager
from selenium import webdriver




class LoginValidation(LoginPage):

    def test_launch_url(self):
        self.open_login_page(url="https://rahulshettyacademy.com/locatorspractice/")
        self.enter_username(locator_type=By.XPATH,locator_value="//input[@id='inputUsername']")
        self.enter_password(locator_type=By.XPATH,locator_value="//input[@name='inputPassword']")
        self.click(locator_type=By.CSS_SELECTOR,locator_value="input[name='inputPassword']")

    def tear_down(self):
        WebDriverManager.quit_browser()


driver = webdriver.Chrome()
obj_validation =LoginValidation(driver)
obj_validation.test_launch_url()
