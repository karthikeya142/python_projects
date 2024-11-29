from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge()
driver.get('https://facebook.com')

emailelement =driver.find_element(By.XPATH,'.//*[@id="email"]')
emailelement.send_keys('karthiksanju2001@gmail.com')
passelement =driver.find_element(By.XPATH,'.//*[@id="pass"]')
passelement.send_keys('Karthikgovardhan@2001')
time.sleep(3)
elem = driver.find_element(By.NAME, 'login')
elem.click()
time.sleep(16)

# statuselement =driver.find_element(By.XPATH,'//*[@name="xhpc_message"]')
# time.sleep(5)
#
# statuselement.send_keys('HI there')
# time.sleep(20)
#
# buttons =driver.find_element(By.TAG_NAME,'button')
# time.sleep(60)
# for button in buttons :
#     if button.text =='Post':
#         button.click()

