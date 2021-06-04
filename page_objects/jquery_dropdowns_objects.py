import time

import pytest
import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JqueryDropdownObject:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)

    DD_with_searchbox = (By.XPATH, "(//span[@class='select2-selection__arrow'])[1]")
    DD_with_searchbox_textfield = (By.XPATH, "//span[@class='select2-search select2-search--dropdown']/input")
    DD_with_searchbox_options = (By.XPATH, "//ul[@class='select2-results__options']/li")
    multi_DD_search_box = (By.XPATH, "//input[@class='select2-search__field']")
    multi_DD_options = (By.XPATH, "//ul[@class='select2-results__options']/li")
    DD_with_disabled_opt = (By.XPATH, "//span[@title='American Samoa']")
    DD_with_disabled_opt_options = (By.XPATH, "//ul[@class='select2-results__options']/li")
    disabled_elements = (By.XPATH, "//ul[@class='select2-results__options']/li[@aria-disabled='true']")
    enabled_elements = (By.XPATH, "//ul[@class='select2-results__options']/li[@aria-selected]")

    def select_dd_value_by_two_char_search(self, initial_chars, expected_country):
        try:
            self.wait.until(EC.visibility_of_element_located((JqueryDropdownObject.DD_with_searchbox)))
            self.driver.find_element(*JqueryDropdownObject.DD_with_searchbox_textfield).send_keys(initial_chars)
        except:
            self.driver.find_element(*JqueryDropdownObject.DD_with_searchbox).click()
            self.driver.find_element(*JqueryDropdownObject.DD_with_searchbox_textfield).send_keys(initial_chars)
        options = self.driver.find_elements(*JqueryDropdownObject.DD_with_searchbox_options)
        print("******", len(options))
        for option in options:
            if option.text.lower() == expected_country.lower():
                option.click()
                break
            else:
                assert False, "State not present in the dropdown"

    def select_multiple_values(self, *states):
        for state in states:
            # self.wait.until(EC.visibility_of_element_located((JqueryDropdownObject.multi_DD_search_box)))
            time.sleep(0.5)
            self.driver.find_element(*JqueryDropdownObject.multi_DD_search_box).send_keys(state)
            for option in self.driver.find_elements(*JqueryDropdownObject.multi_DD_options):
                if option.text.lower() == state.lower():
                    option.click()
                    # time.sleep(2)

    def verify_enabled_and_disabled_count_in_dd(self):
        time.sleep(2)
        self.driver.find_element(*JqueryDropdownObject.DD_with_disabled_opt).click()
        # options = self.driver.find_elements(*JqueryDropdownObject.DD_with_disabled_opt_options)
        disabled_count = len(self.driver.find_elements(*JqueryDropdownObject.disabled_elements))
        enabled_count = len(self.driver.find_elements(*JqueryDropdownObject.enabled_elements))
        assert disabled_count == 2, "Disabled count did not matched expected count"
        assert enabled_count == 4, "Enabled count did not matched expected count"

    def verify_enabled_and_disabled_value(self):
        options = self.driver.find_elements(*JqueryDropdownObject.DD_with_disabled_opt_options)
        disabled_option_value = []
        enabled_option_value = []
        enabled_options = self.driver.find_elements(*JqueryDropdownObject.enabled_elements)
        disabled_options = self.driver.find_elements(*JqueryDropdownObject.disabled_elements)

        for option in disabled_options:
            disabled_option_value.append(option.text)
        for option in enabled_options:
            enabled_option_value.append(option.text)

        assert "American Samoa" in enabled_option_value
        assert "Guam" in disabled_option_value
        assert "Northern Mariana Islands" in enabled_option_value
        assert "Puerto Rico" in enabled_option_value
        assert "United States Minor Outlying Islands" in disabled_option_value
        assert "Virgin Islands" in enabled_option_value
