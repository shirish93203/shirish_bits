from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestAutomation:

    def launch_browser_verify_functionality(self):
        try:
            driver = webdriver.Chrome(executable_path='E:\\Automation directory\\chromedriver.exe')
            driver.get("https://rahulshettyacademy.com/")
            driver.maximize_window()
            time.sleep(5)
        except Exception as e:
            print("Page not load successfully")

object_load = TestAutomation()
object_load.launch_browser_verify_functionality()