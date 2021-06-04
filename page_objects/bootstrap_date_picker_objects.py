import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


class BootstrapDatePickerObject:
    # date_icon = (By.XPATH, "//div[@class='input-group date']/span")
    date_icon = (By.XPATH, "//div[@class='input-group date']/input")
    sunday_dates = (By.XPATH, "//td[7]")
    today = (By.XPATH, "//th[@class='today']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    def click_date_icon(self):
        time.sleep(2)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='input-group date']/input")))
        self.driver.find_element(*BootstrapDatePickerObject.date_icon).click()

    def verify_sunday_dates_is_disabled(self):
        for day in self.driver.find_elements(*BootstrapDatePickerObject.sunday_dates):
            try:
                day.click()
                self.wait.until(EC.element_to_be_selected(day))
                assert False, "sunday date is selected"
            except:
                print("Disabled", day.text)
                assert True, "sunday date is disabled"
    def select_today_date(self):
        self.driver.find_element(*BootstrapDatePickerObject.today).click()
        # time.sleep(2)
        actual_date = self.driver.find_element(*BootstrapDatePickerObject.date_icon).get_attribute('value')
        expected_date = date.today().__format__('%d/%m/%Y')
        assert  actual_date == expected_date , "Date selected with today button is not today's date"
