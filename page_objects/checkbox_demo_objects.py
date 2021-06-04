from selenium import webdriver
from selenium.webdriver.common.by import By

class CheckBox_Demo_Object:

    single_checkbox = (By.XPATH, "(//input[@type='checkbox'])[1]")
    single_checkbox_message = (By.CSS_SELECTOR, "#txtAge")
    multiple_checkbox = (By.XPATH, "(//div[@class='panel panel-default'])[3]//input[@type='checkbox']")
    # multi1 = (By.XPATH, "((//div[@class='panel panel-default'])[3]//input[@type='checkbox'])[1]")
    # multi2 = (By.XPATH, "((//div[@class='panel panel-default'])[3]//input[@type='checkbox'])[2]")
    # multi3 = (By.XPATH, "((//div[@class='panel panel-default'])[3]//input[@type='checkbox'])[3]")
    # multi4 = (By.XPATH, "((//div[@class='panel panel-default'])[3]//input[@type='checkbox'])[4]")
    check_all_btn = (By.XPATH, "//input[@value='Check All']")
    uncheck_all_btn = (By.XPATH, "//input[@value='Uncheck All']")

    def __init__(self, driver):
        self.driver = driver

    def select_single_checkbox(self):
        self.driver.find_element(*CheckBox_Demo_Object.single_checkbox).click()

    def verify_single_checkbox_selection(self):
        selection = self.driver.find_element(*CheckBox_Demo_Object.single_checkbox).is_selected()
        if selection:
            assert True
        else:
            assert  False

    def click_check_all_btn(self):
        self.driver.find_element(*CheckBox_Demo_Object.check_all_btn).click()

    def verify_all_checkbox_are_checked(self):
        for btn in self.driver.find_elements(*CheckBox_Demo_Object.multiple_checkbox):
            if btn.is_selected():
                assert True
            else:
                assert False

    def click_uncheck_all_btn(self):
        self.driver.find_element(*CheckBox_Demo_Object.uncheck_all_btn).click()

    def verify__all_checkbox_are_unchecked(self):
        for btn in self.driver.find_elements(*CheckBox_Demo_Object.multiple_checkbox):
            if btn.is_selected():
                assert False
            else:
                assert True