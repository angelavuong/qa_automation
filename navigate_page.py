from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
driver.get('http://politico.com')
driver.maximize_window()

time.sleep(8)

driver.close()
