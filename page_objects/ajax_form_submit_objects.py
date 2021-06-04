import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AjaxFormSubmitObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    name = (By.ID, "title")
    comment = (By.ID, "description")
    submit_btn = (By.ID, "btn-submit")
    submit_msg = (By.ID, "submit-control")

    def enter_name(self, name):
        self.driver.find_element(*AjaxFormSubmitObject.name).send_keys(name)

    def enter_comment(self, comment):
        self.driver.find_element(*AjaxFormSubmitObject.comment).send_keys(comment)

    def submit_ajax_form(self):
        self.driver.find_element(*AjaxFormSubmitObject.submit_btn).click()

    def verify_submission(self):
        self.wait.until(EC.text_to_be_present_in_element((AjaxFormSubmitObject.submit_msg), "Form submited Successfully!"))
        submission_text = self.driver.find_element(*AjaxFormSubmitObject.submit_msg).text
        assert "Form submited Successfully!" in submission_text
