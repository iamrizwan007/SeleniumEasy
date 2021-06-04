import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import inspect

class MainPageObjects:
    popup = (By.ID, "at-cv-lightbox-close")
    input_form = (By.LINK_TEXT, "Input Forms")
    simple_form_demo = (By.LINK_TEXT, "Simple Form Demo")
    checkbox_demo = (By.LINK_TEXT, "Checkbox Demo")
    radiobutton_demo = (By.LINK_TEXT, "Radio Buttons Demo")
    select_dropdown_list = (By.LINK_TEXT, "Select Dropdown List")
    input_form_submit = (By.LINK_TEXT, "Input Form Submit")
    ajax_form_submit = (By.LINK_TEXT, "Ajax Form Submit")
    jquery_select_dropdown = (By.LINK_TEXT, "JQuery Select dropdown")\

    date_pickers = (By.LINK_TEXT, "Date pickers")
    bootstrap_date_picker = (By.LINK_TEXT, "Bootstrap Date Picker")
    jquery_date_picker = (By.LINK_TEXT, "JQuery Date Picker")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.wait.until(EC.visibility_of_element_located((By.ID, "at-cv-lightbox-close")))
        if self.driver.find_element(*MainPageObjects.popup).is_displayed():
            self.driver.find_element(*MainPageObjects.popup).click()

    def verify_title(self):
        caller = inspect.stack()[1][3]
        if caller == "test_simple_form_demo":
            assert "Simple Form" in self.driver.title
        elif caller == "test_checkbox_demo":
            assert "Checkbox demo" in self.driver.title
        elif caller == "test_radiobutton_demo":
            assert "Radio buttons demo" in self.driver.title
        elif caller == "test_input_form_submit":
            assert "Input Form Demo with Validations" in self.driver.title
        elif caller == "test_ajax_form_submit":
            assert "Ajax Form submit" in self.driver.title
        elif caller == "test_jquery_select_dropdowns":
            assert "JQuery Select and Multi Select" in self.driver.title
        elif caller == "test_bootstrap_date_picker":
            assert "Bootstrap Date picker" in self.driver.title
        elif caller == "test_jquery_date_picker":
            assert "JQuery Date picker" in self.driver.title

    def expand_input_forms(self):
        self.driver.find_element(*MainPageObjects.input_form).click()

    def click_simple_form_demo(self):
        self.driver.find_element(*MainPageObjects.simple_form_demo).click()

    def click_radio_button_demo(self):
        self.driver.find_element(*MainPageObjects.radiobutton_demo).click()

    def click_select_dropdown_list(self):
        self.driver.find_element(*MainPageObjects.select_dropdown_list).click()

    def click_input_form_submit(self):
        self.driver.find_element(*MainPageObjects.input_form_submit).click()

    def click_checkbox_demo(self):
        self.driver.find_element(*MainPageObjects.checkbox_demo).click()

    def click_ajax_form_submit(self):
        self.driver.find_element(*MainPageObjects.ajax_form_submit).click()

    def click_jquery_select_dropdown(self):
        self.driver.find_element(*MainPageObjects.jquery_select_dropdown).click()

    def expand_date_pickers(self):
        self.driver.find_element(*MainPageObjects.date_pickers).click()

    def click_bootstrap_date_picker(self):
        self.driver.find_element(*MainPageObjects.bootstrap_date_picker).click()

    def click_jquery_date_picker(self):
        self.driver.find_element(*MainPageObjects.jquery_date_picker).click()
