import selenium
from selenium.webdriver.common.by import By
import pytest


class RadioButtonDemo:
    male_radio = (By.XPATH, "(//label[@class='radio-inline']/input)[3]")
    female_radio = (By.XPATH, "(//label[@class='radio-inline']/input)[4]")
    age_0_to_5 = (By.XPATH, "(//label[@class='radio-inline']/input)[5]")
    age_5_to_15 = (By.XPATH, "(//label[@class='radio-inline']/input)[6]")
    age_15_to_50 = (By.XPATH, "(//label[@class='radio-inline']/input)[7]")
    get_value_btn = (By.XPATH, "//button[@onclick='getValues();']")

    def __init__(self, driver):
        self.driver = driver

    def select_radio_buttons(self, gender, age):
        if gender.lower() == "male":
            self.driver.find_element(*RadioButtonDemo.male_radio).click()
        elif gender.lower() == "female":
            self.driver.find_element(*RadioButtonDemo.female_radio).click()

        if age > 0 and age < 5:
            self.driver.find_element(*RadioButtonDemo.age_0_to_5).click()
        elif age>=5 and age <= 15:
            self.driver.find_element(*RadioButtonDemo.age_5_to_15).click()
        elif age>15 and age<50:
            self.driver.find_element(*RadioButtonDemo.age_15_to_50).click()

    def click_on_get_values(self):
        self.driver.find_element(*RadioButtonDemo.get_value_btn).click()
