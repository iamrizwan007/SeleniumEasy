from selenium import webdriver
import pytest
from page_objects.main_page import MainPageObjects
from page_objects.bootstrap_date_picker_objects import BootstrapDatePickerObject

@pytest.mark.usefixtures("setup")
class TestDatePickers:

    def test_bootstrap_date_picker(self):
        main_page_obj = MainPageObjects(self.driver)
        main_page_obj.expand_date_pickers()
        main_page_obj.click_bootstrap_date_picker()
        main_page_obj.verify_title()
        bootstrap_obj = BootstrapDatePickerObject(self.driver)
        bootstrap_obj.click_date_icon()
        bootstrap_obj.verify_sunday_dates_is_disabled()
        bootstrap_obj.select_today_date()