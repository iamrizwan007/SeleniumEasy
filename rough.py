from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/s?k=bose+speakers&ref=nb_sb_noss_1")
bose_checkbox = driver.find_element(By.XPATH, "//li[@aria-label='Bose']//div")
bose_checkbox.click()
dropdown = driver.find_element(By.CLASS_NAME, "a-dropdown-container")
dropdown.click()
avg_cust = driver.find_element(By.XPATH, "//li[@class='a-dropdown-item']/a[@id='s-result-sort-select_3']")
avg_cust.click()
item_names = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
item_price = driver.find_elements(By.XPATH, "//div[@class='a-row a-size-base a-color-base']")
items = []
for i in range(len(item_names)):
    temp={}
    temp[item_names[i].text] = item_price[i].text
    items.append(temp)
print(items)
