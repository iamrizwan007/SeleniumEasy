import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SelectDropdownListObject:
    single_dropdown = (By.ID, "select-demo")
    multi_dropdown = (By.ID, "multi-select")

    def __init__(self, driver):
        self.driver = driver

    def select_value(self, day):
        option = Select(self.driver.find_element(*SelectDropdownListObject.single_dropdown))
        option.select_by_visible_text(day.lower().capitalize())

    def select_values(self,*args):
        option = Select(self.driver.find_element(*SelectDropdownListObject.multi_dropdown))
        for arg in args:
            option.select_by_visible_text(arg)
