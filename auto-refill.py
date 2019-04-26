##
## Prerequisite
## pip install inflect
## pip install selenium
##
## TODO:
## Pass in the path to your chrome profile
## Update your debit card number
## 
## Before start
## Open page https://www.amazon.com/asv/reload/order?_encoding=UTF8&ref_=gc_cac_red
## and make sure you are signed in. Otherwise sign in and check 'Keep me signed in'.
## Make sure you have no chrome instance opened, otherwise chrome will crash

import time
import inflect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        seconds = seconds - 1
        time.sleep(1)
    print("Start")

def enterEmail(email):
    email_field = driver.find_element_by_id('ap_email')
    email_field.send_keys(email)
    
def enterPassword(password):
    password_field = driver.find_element_by_id('ap_password')
    password_field.send_keys(password)

def launch():
    chrome_options = webdriver.ChromeOptions()
    ## Enter path for your profile
    chrome_options.add_argument(r"--user-data-dir=C:\Users\<your name>\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument(r"--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def main(amount, times):
    print('About to refill your amazon account. ${} one time, {} times in total.'.format(amount, times))
    print('If this is incorrect, press Ctrl + C immediately')
    countdown(10)
    
    inflect_eng = inflect.engine()
    driver = launch()
    driver.get('https://www.amazon.com/asv/reload/order?_encoding=UTF8&ref_=gc_cac_red')
    wait = WebDriverWait(driver, 5)
    wait.until(ec.presence_of_element_located((By.ID, 'asv-manual-reload-amount')))
    
    try:
        for t in range(times):
            amount_text = driver.find_element_by_id('asv-manual-reload-amount')
            amount_text.send_keys(str(amount))
            ## Wait for seconds since the amount is important
            time.sleep(5)
            submit_button = driver.find_element_by_id('form-submit-button')
            submit_button.click()
            print(inflect_eng.ordinal(t) + ' refill submitted with $' + str(amount))
            wait = WebDriverWait(driver, 5)
            wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'a-alert-success')))
            ## Update to your master card last 4 digits
            wait.until(ec.presence_of_element_located((By.XPATH, '//div[contains(text(), "MasterCard ending in <your debit card last 4 digits>")]')))
            print('Success')
            time.sleep(2)
            driver.back()
    finally:
        driver.quit()

if __name__== "__main__":
  main(amount=0.5, times=12)




    
