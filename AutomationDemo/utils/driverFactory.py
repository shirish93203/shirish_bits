from selenium import webdriver

#This class is used to initiate the webdriver and ensure only one instance has been created

class WebDriverManager:
    driver = None

    @staticmethod
    def get_driver(browser='browser'):
        if WebDriverManager.driver is None:
            if browser =='chrome':
                WebDriverManager.driver =webdriver.chrome
            elif browser =='safari':
                WebDriverManager.driver = webdriver.safari
            elif browser =='IE':
                WebDriverManager.driver = webdriver.ie

        WebDriverManager.driver.maximize_window()
        WebDriverManager.driver.implicit_wait(10)

        return  WebDriverManager.driver

    @staticmethod
    def quit_browser():
        if WebDriverManager.driver is not None:
            WebDriverManager.driver.quit()
            WebDriverManager.driver = None





