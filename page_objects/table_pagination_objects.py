import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TablePagination:
    table_headings = (By.CSS_SELECTOR, "th")
    table_rows = (By.XPATH, "//tr[@style='display: table-row;']")
    active_page = (By.XPATH, "//li[@class='active']/a")
    next_page = (By.XPATH, "//a[@class='next_link']")
    last_page = (By.XPATH, "//a[@class='next_link' and @style='display: none;']")

    def __init__(self, driver):
        self.driver = driver

    def verify_table(self):
        headers = len(self.driver.find_elements(*TablePagination.table_headings))
        assert headers == 7
        rows = len(self.driver.find_elements(*TablePagination.table_rows))
        assert rows >= 1

    def verify_table_pagination(self):
        count = 1
        next_icon = self.driver.find_element(*TablePagination.next_page)
        while next_icon:
            self.verify_table()
            current_page = self.driver.find_element(*TablePagination.active_page).text
            assert int(current_page) == count
            count = count + 1
            try:
                self.driver.find_element(*TablePagination.last_page).is_displayed()
                print("element found and loop broken")
                break
            except NoSuchElementException:
                next_icon.click()
