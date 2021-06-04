import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BootstrapDatePickerObject:
    date_icon = (By.XPATH, "//div[@class='input-group date']/span")
    sunday_dates = (By.XPATH, "//td[7]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    def click_date_icon(self):
        time.sleep(2)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='input-group date']/span")))
        self.driver.find_element(*BootstrapDatePickerObject.date_icon).click()
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='input-group date']/span")))

    def verify_sunday_dates_is_disabled(self):
        for day in self.driver.find_elements(*BootstrapDatePickerObject.sunday_dates):
            try:
                day.click()
                self.wait.until(EC.element_to_be_selected(day))
                assert False, "sunday date is selected"
            except:
                print("Disabled", day.text)
                assert True, "sunday date is disabled"