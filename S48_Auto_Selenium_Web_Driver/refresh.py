from time import sleep
import time
from selenium  import webdriver

driver =webdriver.Edge()
driver.get('https://www.google.com')
time.sleep(15)
driver.refresh()