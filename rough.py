from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.techwithtim.net/?s=test"

## Driver setup and access title

path = "../dater/driver/chromedriver"
driver = webdriver.Chrome()
driver.get(url)

## Extract main from the new page and then headers

main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "main"))
)
#print(main.text)
articles = main.find_elements_by_tag_name("article")
print(len(articles))
# header.append(articles[0].find_element_by_tag_name("a").text)
header =articles[0].find_element_by_tag_name("a").get_attribute('text')
print(header)