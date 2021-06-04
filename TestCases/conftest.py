import time

from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", default="chrome"
    )

@pytest.fixture()
def setup(request):
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\Rizwan\\Desktop\\WebScccrinnngg\\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path= "")
    elif browser == "edge":
        driver = webdriver.Edge(executable_path="")
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='60%'")
    driver.get("https://www.seleniumeasy.com/test/")
    request.cls.driver = driver

# pytest HTML reporting
# def pytest_configure(config):
#     config._metadeta['Project Name'] = 'Selenium Easy'
#     config._metadata['Environment'] = 'QA2'
#     config._metadata['Sprint'] = 'Sprint 2'
#     config._metadata['Tester'] = 'Mohammad Rizwan'

# # hook to remove default environment info
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
