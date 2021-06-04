from datetime import date

today = date.today()
year = today.year
month = today.month
day = today.day
print("Today's date:", str(day) + str(month) + str(year))
wait = WebDriverWait(driver,10)
from selenium.webdriver.support import expected_conditions as ec
try:
    sun.click()
    wait.until(ec.element_to_be_selected((By.XPATH,"(//td[7])[1]")))
except:
    print("exception")
