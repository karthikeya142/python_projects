import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver =webdriver.Edge()
driver.get('https://google.com')
time.sleep(2)
elem =driver.find_element(By.LINK_TEXT,'About')
time.sleep(2)
elem.click()
time.sleep(2)
# elem.send_keys(Keys.END)
# time.sleep(5)
# elem.send_keys(Keys.HOME)
# time.sleep(5)
print(driver.current_url)