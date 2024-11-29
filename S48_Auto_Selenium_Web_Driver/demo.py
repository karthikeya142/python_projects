# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# # Initialize the WebDriver
# driver = webdriver.Chrome()
#
# # Open Google homepage
# driver.get('http://www.google.com')
# time.sleep(2)  # Wait for the page to load
#
# # Locate the Google search bar using the name attribute "q"
# search_bar = driver.find_element(By.NAME, 'q')
#
# # Clear the search bar in case there's any default text (usually empty on Google)
# search_bar.clear()
#
# # Enter search term
# search_bar.send_keys("Python3")
#
# # Simulate pressing Enter to initiate search
# search_bar.send_keys(Keys.RETURN)
#
# # Wait to see the search results
# time.sleep(5)
#
# # Close the browser
# driver.quit()







import time

from selenium import webdriver

from time import sleep

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('https://www.google.com')
time.sleep(5)
# elem = driver.find_element(By.NAME,'q')
elem =driver.find_element(By.LINK_TEXT,'About')
elem.click()
time.sleep(5)

elem =driver.find_element(By.LINK_TEXT,'Products')
elem.click()
time.sleep(5)

elem =driver.find_element(By.LINK_TEXT,'Commitments')
elem.click()
time.sleep(10)

elem =driver.find_element(By.LINK_TEXT,'Stories')
elem.click()
time.sleep(15)

elem =driver.find_element(By.LINK_TEXT,'India Blog')
elem.click()
time.sleep(20)

# elem = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
# elem.clear()
# elem.send_keys("https://www.facebook.com/katthik.govardhan/")
# elem.send_keys(Keys.RETURN)

driver.quit()