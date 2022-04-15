from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class TestAutomation:

    def launch_browser_verify_functionality(self):
        try:
            driver = webdriver.Chrome(executable_path='E:\\Automation directory\\chromedriver.exe')
            driver.get("https://rahulshettyacademy.com/")
            driver.maximize_window()
            time.sleep(5)
            if driver.current_url!="https://rahulshettyacademy.com/#/index":
                raise ("Page not laod successfully")
            else:
                driver.find_element(by=By.XPATH,
                                       value="//div[@class='login-btn']/a[@class='theme-btn register-btn']").click()  # Identified webelement using Xpath
                time.sleep(5)
                driver.find_element(by=By.NAME, value="email").send_keys("2021mt93264@wilp.bits-pilani.ac.in")
                driver.find_element(by=By.NAME, value="password").send_keys("oneIlmg@12")
                driver.find_element(by=By.NAME, value="commit").click()
                time.sleep(3)
                driver.find_element(by=By.XPATH,
                                    value="(//div[@class='navbar-collapse collapse clearfix']/ul/li/a[contains(text(),'Practice')])[1]").click()
                driver.find_element(by=By.NAME, value="name").send_keys("Roja")
                driver.find_element(by=By.NAME, value="email").send_keys("2021mt93264@wilp.bits-pilani.ac.in")
                time.sleep(15)
                driver.find_element(by=By.XPATH,
                                    value="//button[@id ='form-submit']").click()  # Identified webelement using Xpath
                time.sleep(5)
                driver.find_element(by=By.XPATH,
                                    value="//div[@class='projects-item']/a[contains(text(),'Automation Practise - 2')]").click()
                time.sleep(5)
                list_count = driver.find_elements(by=By.XPATH, value="//legend[contains(text(),'Web Table Fixed header')]/../div/table/thead/tr")
                print(len(list_count))

        except Exception as e:
            print("Page not load successfully")

object_load = TestAutomation()
object_load.launch_browser_verify_functionality()