# INSTRUCTIONS:
# run combine-billing.py first on a csv downloaded from Smokeball Billing
# 1. On Smokeball Billing in Chrome, click on a matter
# 2. Copy the URL, and enter when prompted
# 3. enter the filename of the output from combine-billing.py
#
# This will output a csv with time and descriptions of the same day added together

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import pandas as pd

import time


URL = input("Enter the URL of the page to add time entries: ")
CSV = input("Enter the filename of the CSV to get info from: ")

df = pd.read_csv(CSV)

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

for index, row in df.iterrows():

    new_entry_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/sb-compose/div/ng-transclude/div[2]/div/div[2]/div/sb-matter-view/sb-compose/div/ng-transclude/div[3]/sbb-matter-fee-entries/div/div[1]/div[1]/button')))
    new_entry_button.click()
    time.sleep(0.2)

    staff_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/form/fieldset/div/div[1]/div[1]/div[1]/div[2]/sb-staff-selector/div/input')
    staff_field.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
    staff_field.send_keys("Mark K Smallhouse", Keys.RETURN)
    time.sleep(0.2)

    date = str(row['Date'])
    date_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/form/fieldset/div/div[1]/div[1]/div[1]/div[1]/div/sb-datepicker/sbb-date-picker/div/div/input')
    date_field.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
    date_field.send_keys(date)
    time.sleep(0.2)

    subject = row['Subject']
    subject_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/form/fieldset/div/div[1]/div[1]/div[3]/div[2]/div/sb-activity-subject-typeahead/input')
    subject_field.send_keys(subject)
    time.sleep(0.2)

    hours = row['Hours']
    hours_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/form/fieldset/div/div[1]/div[1]/div[4]/div[1]/div/input')
    hours_field.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
    hours_field.send_keys(hours)
    time.sleep(0.2)

    description = row['Description']
    description_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/form/fieldset/div/div[1]/div[1]/div[6]/div/div/textarea')
    description_field.send_keys(description)
    time.sleep(0.2)

    save_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/form/fieldset/div/div[2]/div/div[1]/button')
    save_button.click()
    time.sleep(0.5)

#close browser
driver.quit()