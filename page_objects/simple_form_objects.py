import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import inspect

class SimpleFormPageObjects:
    simple_form_message_box = (By.XPATH, "//input[@id='user-message']")
    simple_form_message_verify = (By.XPATH, "//span[@id='display']")
    simple_num1 = (By.XPATH, "//input[@id='sum1']")
    simple_num2 = (By.XPATH, "//input[@id='sum2']")
    simple_total_btn = (By.XPATH, "//button[text()='Get Total']")
    simple_total_result = (By.XPATH, "//span[@id='displayvalue']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def single_input_message(self, msg):
        self.driver.find_element(*SimpleFormPageObjects.simple_form_message_box).send_keys(msg)
        self.driver.find_element(By.XPATH, "//button[text()='Show Message']").click()

    def verify_single_input_message(self, msg):
        assert msg == self.driver.find_element(*SimpleFormPageObjects.simple_form_message_verify).text

    def single_input_num1(self, number):
        self.driver.find_element(*SimpleFormPageObjects.simple_num1).send_keys(number)

    def single_input_num2(self, number):
        self.driver.find_element(*SimpleFormPageObjects.simple_num2).send_keys(number)

    def click_on_total(self):
        self.driver.find_element(*SimpleFormPageObjects.simple_total_btn).click()

    def verify_total_sum(self, number1, number2):
        total = self.driver.find_element(*SimpleFormPageObjects.simple_total_result).text
        if number1+number2 == int(total):
            assert True
        else:
            assert False, "Total did not matched"