import pytest
from selenium import webdriver
from AutomationDemo.utils.driverFactory import WebDriverManager

pytest.fixture(scope='function')
def setup(request):
    browser = request.config.getoption("--browser")
    return request,browser

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome, firefox, or edge")





