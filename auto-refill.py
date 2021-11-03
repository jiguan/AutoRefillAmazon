##
## Prerequisite
## pip install inflect
## pip install selenium
## pip install webdriver-manager
##
## TODO:
## Pass in the path to your chrome profile
## Update your debit card number
## 
## Before start
## Open page https://www.amazon.com/gp/product/B086KKT3RX
## and make sure you are signed in. Otherwise sign in and check 'Keep me signed in'.
## Make sure you have no chrome instance opened, otherwise chrome will crash

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

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
    chrome_options.add_argument(r"--user-data-dir=C:\Users\{your_name}\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument(r"--no-sandbox")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver

def main(amount, times):
    print('About to refill your amazon account. ${} one time, {} times in total.'.format(amount, times))
    print('If this is incorrect, press Ctrl + C immediately')
    countdown(3)

    driver = launch()
    wait = WebDriverWait(driver, 5)

    try:
        for t in range(times):
            driver.get('https://www.amazon.com/gp/product/B086KKT3RX')
            amt_input =  wait.until(ec.presence_of_element_located((By.ID, 'gcui-asv-reload-form-custom-amount')))
            amt_input.send_keys(str(amount))
            driver.find_element_by_xpath("//input[@type='submit' and @name='submit.gc-buy-now']").click()
            # Update care number here
            wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(), '4785')]")))
            wait.until(ec.presence_of_element_located((By.ID, 'placeYourOrder')))
            driver.find_element(By.XPATH, "//input[@type='submit' and @name='placeYourOrder1']").click()
            countdown(1)
            print("{} time refill is done".format(t))
        print("All {} times refill completed successfully".format(times))
    finally:
        driver.quit()

if __name__== "__main__":
  main(amount=0.5, times=12)