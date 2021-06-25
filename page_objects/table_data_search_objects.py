import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TableDataSearch:
    search = (By.ID, "task-table-filter")
    search_by_status = (By.XPATH, "//table[@class='table table-hover']//tr[@style='display: table-row;']/td[4]")

    def __init__(self, driver):
        self.driver = driver

    def search_by(self, status):
        time.sleep(3)
        self.driver.find_element(*TableDataSearch.search).send_keys(status)
        time.sleep(2)
        statuses = self.driver.find_elements(*TableDataSearch.search_by_status)
        for stat in statuses:
            print("checking", stat.get_attribute("value"))
