import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class InputFormSubmitObject:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)

    fname = (By.NAME, "first_name")
    lname = (By.NAME, "last_name")
    email = (By.NAME, "email")
    phone = (By.NAME, "phone")
    address = (By.NAME, "address")
    city = (By.NAME, "city")
    state_sel = (By.XPATH, "//select[@name='state']")
    zip = (By.NAME, "zip")
    website = (By.NAME, "website")
    hosting_elements = (By.XPATH, "//input[@name='hosting']")
    description = (By.NAME, "comment")
    send_btn = (By.XPATH, "//button[@class='btn btn-default']")

    def  enter_first_name(self, first_name):
        try:
            self.wait.until(EC.visibility_of_element_located((InputFormSubmitObject.fname)))
            self.driver.find_element(*InputFormSubmitObject.fname).send_keys(first_name)
        except :
            print("exception did not handled - first name")


    def enter_last_name(self, last_name):
        self.driver.find_element(*InputFormSubmitObject.lname).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*InputFormSubmitObject.email).send_keys(email)

    def enter_phone_number(self,phone):
        self.driver.find_element(*InputFormSubmitObject.phone).send_keys(phone)

    def enter_address(self, address):
        self.driver.find_element(*InputFormSubmitObject.address).send_keys(address)

    def enter_city(self,city):
        self.driver.find_element(*InputFormSubmitObject.city).send_keys(city)

    def select_state(self, state):
        option = Select(self.driver.find_element(*InputFormSubmitObject.state_sel))
        option.select_by_visible_text(state)

    def enter_zip(self,zip):
        self.driver.find_element(*InputFormSubmitObject.zip).send_keys(zip)

    def enter_website(self,website):
        self.driver.find_element(*InputFormSubmitObject.website).send_keys(website)

    def set_hosting(self, set_option):
        for option in self.driver.find_elements(*InputFormSubmitObject.hosting_elements):
            if option.get_attribute("value") == set_option:
                option.click()

    def enter_project_description(self, description):
        self.driver.find_element(*InputFormSubmitObject.description).send_keys(description)

    def click_on_submit_button(self):
        self.driver.find_element(*InputFormSubmitObject.send_btn).click()
