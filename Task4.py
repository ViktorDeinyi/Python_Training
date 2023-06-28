# Task4 'http://the-internet.herokuapp.com'  testing

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "http://the-internet.herokuapp.com/"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)

# checkboxes
checkbox = driver.find_element(By.LINK_TEXT, 'Checkboxes')
checkbox.click()
checkbox1 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
checkbox1.click()
checkbox2 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
checkbox2.click()
assert checkbox1.is_selected()
assert not checkbox2.is_selected()
driver.back()

# file download
file_download = driver.find_element(By.LINK_TEXT, 'File Download')
file_download.click()
file_to_download = driver.find_element(By.XPATH, '//*[@id="content"]/div/a[1]')
path1 = os.path.join('/Users/viktordeynyy/Downloads/', file_to_download.text)
file_to_download.click()
time.sleep(25)
assert os.path.isfile(path1)
os.remove(path1)
driver.back()

# file upload
file_name = 'IMG_8625.jpeg'
file_upload = driver.find_element(By.LINK_TEXT, 'File Upload')
file_upload.click()
choose_file = driver.find_element(By.ID, 'file-upload')
choose_file.send_keys('/Users/viktordeynyy/Desktop/' + file_name)
driver.find_element(By.ID, 'file-submit').submit()
assert driver.find_element(By.ID, 'uploaded-files').text in file_name
driver.back()
driver.back()

# hovers
hovers = driver.find_element(By.LINK_TEXT, 'Hovers')
hovers.click()
a = ActionChains(driver)
first_hover = driver.find_elements(By.CLASS_NAME, 'figure')[1]
a.move_to_element(first_hover).perform()
assert driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/h5').is_displayed()
driver.back()

# dropdown
file_download = driver.find_element(By.LINK_TEXT, 'Dropdown')
file_download.click()
dropdown = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option')
dropdown1 = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[2]')
dropdown2 = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[3]')
assert dropdown.text in 'Please select an option'
assert dropdown.is_selected()
dropdown.click()
dropdown1.click()
assert dropdown1.is_selected()
dropdown2.click()
assert dropdown2.is_selected()
driver.back()

# dynamic loading (1)
dynamic_loading = driver.find_element(By.LINK_TEXT, 'Dynamic Loading')
dynamic_loading.click()
dynamic_loading_hidden_el = driver.find_element(By.XPATH, '//*[@id="content"]/div/a[1]')
dynamic_loading_hidden_el.click()
start1 = driver.find_element(By.XPATH, '//*[@id="start"]/button')
result1 = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
assert result1.is_enabled()
assert not result1.is_displayed()
start1.click()
WebDriverWait(driver, 10).until(EC.visibility_of(result1))
assert result1.is_displayed()
assert result1.text in 'Hello World!'
driver.back()
# dynamic loading (2)
dynamic_loading_rendered_el = driver.find_element(By.XPATH, '//*[@id="content"]/div/a[2]')
dynamic_loading_rendered_el.click()
start2 = driver.find_element(By.XPATH, '//*[@id="start"]/button')
result2_xpath = '//*[@id="finish"]/h4'
try:
    result2 = driver.find_element(By.XPATH, result2_xpath)
except NoSuchElementException:
    print('Element result2 is missing before pushing start button')
start2.click()
result2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, result2_xpath)))
assert result2.is_displayed()
print('Element result2 is present after pushing start button')
assert result2.text in 'Hello World!'

driver.close()
driver.quit()