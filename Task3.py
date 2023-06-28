# try to create script with webdriver chrome which search via google softserve website and open it)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.google.com/"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)
search_field = driver.find_element(By.NAME, 'q')
search_field.send_keys("SoftServe")
search_field.send_keys(Keys.ENTER)
try:
    first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rso"]//div['
                                                                                             '1]/a/h3')))
    first_result.click()
except:
    print("Do not find element")
driver.close()
driver.quit()
