import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://google.com')

# Locate Google Search Box
search = driver.find_element_by_id('lst-ib')

# Search Phrase
search.send_keys('Python 3')

# 'ENTER' for Search
search.send_keys(Keys.RETURN)
time.sleep(6)

# Clears Search
search.clear()
time.sleep(2)

driver.close()
