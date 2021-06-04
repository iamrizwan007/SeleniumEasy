import logging
from selenium import webdriver
from page_objects.ajax_form_submit_objects import AjaxFormSubmitObject
from page_objects.input_form_submit_objects import InputFormSubmitObject
from page_objects.jquery_dropdowns_objects import JqueryDropdownObject
from page_objects.main_page import MainPageObjects
from page_objects.select_dropdown_list_objects import SelectDropdownListObject
from page_objects.simple_form_objects import SimpleFormPageObjects
from page_objects.checkbox_demo_objects import CheckBox_Demo_Object
from page_objects.radio_button_demo_objects import RadioButtonDemo
from Utilities.Base import BaseClass
from TestData.statelist import StateListData
import pytest
import allure
from allure_pytest.listener import AttachmentType

@pytest.mark.usefixtures("setup")
class TestInputForms:

    @pytest.fixture(params=StateListData.getstate)
    def getstatedata(self, request):
        return request.param

    @pytest.mark.skip
    def test_simple_form_demo(self):
        mylogger = BaseClass.getCustomLogger(logging.INFO)
        mylogger.info("test_simple_form_demo started.......")
        main_page_obj = MainPageObjects(self.driver)
        simple_form_page_obj = SimpleFormPageObjects(self.driver)
        main_page_obj.expand_input_forms()
        mylogger.info("Expanded input forms")
        main_page_obj.click_simple_form_demo()
        mylogger.info("clicked on simple form demo")
        main_page_obj.verify_title()
        mylogger.info("Title verified")
        msg = "testing message"
        simple_form_page_obj.single_input_message(msg)
        simple_form_page_obj.verify_single_input_message(msg)
        num1 = 10
        num2 = 20
        simple_form_page_obj.single_input_num1(num1)
        simple_form_page_obj.single_input_num2(num2)
        simple_form_page_obj.click_on_total()
        simple_form_page_obj.verify_total_sum(num1, num2)

    @pytest.mark.skip
    def test_checkbox_demo(self):
        mylogger = BaseClass.getCustomLogger(logging.INFO)
        mylogger.info("test_checkbox_demo started.....")
        main_page_obj = MainPageObjects(self.driver)
        mylogger.info("Main page object created..")
        main_page_obj.expand_input_forms()
        main_page_obj.click_checkbox_demo()
        mylogger.info("Clicked on the checkbox demo..Verifying title")
        main_page_obj.verify_title()
        mylogger.info("title verified")
        checkboox_obj = CheckBox_Demo_Object(self.driver)
        checkboox_obj.select_single_checkbox()
        checkboox_obj.verify_single_checkbox_selection()
        checkboox_obj.click_check_all_btn()
        checkboox_obj.verify_all_checkbox_are_checked()
        checkboox_obj.click_uncheck_all_btn()
        checkboox_obj.verify__all_checkbox_are_unchecked()

    @pytest.mark.skip
    def test_radiobutton_demo(self):
        mylogger = BaseClass.getCustomLogger(logging.INFO)
        main_page_obj = MainPageObjects(self.driver)
        main_page_obj.expand_input_forms()
        main_page_obj.click_radio_button_demo()
        main_page_obj.verify_title()
        radiobutton_obj = RadioButtonDemo(self.driver)
        radiobutton_obj.select_radio_buttons('male', 45)
        radiobutton_obj.click_on_get_values()

    @pytest.mark.skip
    def test_select_dropdown_list(self):
        mylogger = BaseClass.getCustomLogger(logging.INFO)
        main_page_obj = MainPageObjects(self.driver)
        main_page_obj.expand_input_forms()
        main_page_obj.click_select_dropdown_list()
        selectobj = SelectDropdownListObject(self.driver)
        selectobj.select_value("MONDAY")
        selectobj.select_values("California", "New York")

    @pytest.mark.skip
    def test_input_form_submit(self):
        mylogger = BaseClass.getCustomLogger(logging.INFO)
        main_page_obj = MainPageObjects(self.driver)
        main_page_obj.expand_input_forms()
        main_page_obj.click_input_form_submit()
        main_page_obj.verify_title()
        input_form_submit_obj = InputFormSubmitObject(self.driver)
        input_form_submit_obj.enter_first_name("Mohammad")
        input_form_submit_obj.enter_last_name("Rizwan")
        input_form_submit_obj.enter_email("test@testing.com")
        input_form_submit_obj.enter_phone_number("7894561236")
        input_form_submit_obj.enter_address("test address")
        input_form_submit_obj.enter_city("New Delhi")
        input_form_submit_obj.select_state("New York")
        input_form_submit_obj.enter_zip("01001")
        input_form_submit_obj.enter_website("www.python.org")
        input_form_submit_obj.set_hosting("yes")
        input_form_submit_obj.enter_project_description("test description")

    @pytest.mark.skip
    def test_ajax_form_submit(self):
        mylogger = BaseClass.getCustomLogger(logging.INFO)
        main_page_obj = MainPageObjects(self.driver)
        main_page_obj.expand_input_forms()
        main_page_obj.click_ajax_form_submit()
        main_page_obj.verify_title()
        ajax_form_obj = AjaxFormSubmitObject(self.driver)
        ajax_form_obj.enter_name("Rizwan")
        ajax_form_obj.enter_comment("This is the test comment")
        ajax_form_obj.submit_ajax_form()
        ajax_form_obj.verify_submission()

    @pytest.mark.skip
    def test_jquery_select_dropdowns(self, getstatedata):
        mylogger = BaseClass.getCustomLogger(logging.INFO)
        main_page_obj = MainPageObjects(self.driver)
        main_page_obj.expand_input_forms()
        main_page_obj.click_jquery_select_dropdown()
        main_page_obj.verify_title()
        jquery_dd_obj = JqueryDropdownObject(self.driver)
        jquery_dd_obj.select_dd_value_by_two_char_search("in","India")

        # Multiple values
        jquery_dd_obj.select_multiple_values(
            getstatedata.get('state1'),
            getstatedata.get('state2')
        )

    @pytest.mark.skip
    def test_dropdown_with_disabled_option(self):
        mylogger = BaseClass.getCustomLogger(logging.INFO)
        main_page_obj = MainPageObjects(self.driver)
        main_page_obj.expand_input_forms()
        main_page_obj.click_jquery_select_dropdown()
        main_page_obj.verify_title()
        jquery_dd_obj = JqueryDropdownObject(self.driver)
        jquery_dd_obj.verify_enabled_and_disabled_count_in_dd()
        jquery_dd_obj.verify_enabled_and_disabled_value()