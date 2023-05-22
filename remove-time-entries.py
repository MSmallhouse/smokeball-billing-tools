# INSTRUCTIONS: 
# 1. Navigate to a draft bill on Smokeball Billing in Chrome
# 2. Make sure you're on the draft page where you can edit time entries
# 3. Copy the URL and enter when prompted
#
# All of the time entried for this bill will be deleted.
# BE CAREFUL, these cannot be recovered

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

URL = input("Enter URL of the bill to delete fees from: ")

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#implicit wait
driver.implicitly_wait(0.5)
#launch URL
driver.get(URL)

# login
email = driver.find_element(By.XPATH, '//*[@id="content"]/div/sbb-login-route/div/div[2]/div/fieldset/div[1]/input')
email.send_keys("matthewsmallhouse@gmail.com")
password = driver.find_element(By.XPATH, '//*[@id="content"]/div/sbb-login-route/div/div[2]/div/fieldset/div[2]/input')
password.send_keys("Cortina2@")
enter = driver.find_element(By.XPATH, '//*[@id="content"]/div/sbb-login-route/div/div[2]/div/fieldset/div[4]/button')
enter.click()

wait = WebDriverWait(driver, 60)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.icon.icon-compile')))

button_list = driver.find_elements(By.CSS_SELECTOR, 'span.icon.icon-compile')

for i in range(len(button_list)):
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.icon.icon-compile')))
    button.click()
    time.sleep(0.3)
    remove = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div/form/fieldset/div/div[1]/div[1]/div[7]/div/div/a')))
    remove.click()
    time.sleep(0.3)




#close browser
driver.quit()