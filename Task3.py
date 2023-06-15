#try to create script with webdriver chrome which search via google softserve website and open it)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

url = "https://www.google.com/"
driver = webdriver.Chrome()

driver.get(url=url)
time.sleep(2)
search_field = driver.find_element(by=By.NAME, value='q')
search_field.send_keys("SoftServe")
search_field.send_keys(Keys.ENTER)
first_result = driver.find_element(by=By.XPATH, value='//*[@id="rso"]//div[1]/a/h3')
first_result.click()
time.sleep(2)

driver.close()
driver.quit()