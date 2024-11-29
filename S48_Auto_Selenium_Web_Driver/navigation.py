from time import sleep
import time
from selenium  import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Edge()
driver.get('https://www.google.com')
time.sleep(2)
elem=driver.find_element(By.LINK_TEXT,'About')
time.sleep(5)
elem.click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)