# ------------------------------STEPS BEFORE RUNNING THE CODE:
# Commands to do:
# pip install selenium
# pip install pyautogui

# put the chromedriver.exe in C:\Program Files (x86)
# put th folder 'warehouses' in the C:\
# change the emai and the password in the lines 26 and 29

# --------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import os
import time

driver = webdriver.Chrome()

# -----------Login
driver.get("http://mywebsite.localhost:8000/#login")
#  setWindowSize | 1296x796 |
driver.set_window_size(1296, 796)

#  id=login_email | manouha251@gmail.com
driver.find_element(By.ID, "login_email").send_keys("manouha251@gmail.com")
time.sleep(1)
#  id=login_password | MaNo1234
driver.find_element(By.ID, "login_password").send_keys("MaNo1234")
time.sleep(1)
# click | css=.btn-login |
driver.find_element(By.CSS_SELECTOR, ".btn-login").click()
time.sleep(3)
folder_path = "C:/warehouses/"
# Get the list of all files in the directory
all_files = os.listdir(folder_path)
for file_name in all_files:
    driver.get("http://mywebsite.localhost:8000/app/home")
    file_path = os.path.join(folder_path, file_name)
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    element1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@id=\'editorjs\']/div/div/div[13]/div/div/div/div[2]/a/span[2]")))
    element1.click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn-primary > .hidden-xs").click()
    time.sleep(3)

    # Insert warehouse
    driver.find_element(By.CSS_SELECTOR, ".awesomplete > .input-with-feedback").send_keys("Warehouse")
    time.sleep(2)

    # select | css=.flex > .input-with-feedback | label=Insert New Records
    dropdown = driver.find_element(By.CSS_SELECTOR, ".flex > .input-with-feedback")
    dropdown.find_element(By.XPATH, "//option[. = 'Insert New Records']").click()
    time.sleep(2)

    #  click | css=.form-group:nth-child(3) .input-area |
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) .input-area").click()
    # click | css=.standard-actions:nth-child(3) > .btn-primary |
    driver.find_element(By.CSS_SELECTOR, ".standard-actions:nth-child(3) > .btn-primary").click()
    time.sleep(2)

    # btn-attach
    driver.find_element(By.CSS_SELECTOR, ".btn-attach").click()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1) circle").click()

    # Locate the file input element and send the file path to it
    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(file_path)
    time.sleep(2)
    # Use pyautogui to send 'esc' key, which will close the file explorer
    pyautogui.press('esc')

    # Upload button
    driver.find_element(By.CSS_SELECTOR, ".btn-modal-primary").click()
    time.sleep(5)

    # Start Import button
    for _ in range(3):  # Loop 3 times
        element = driver.find_element(By.XPATH, "//div[@id='page-Data Import']/div/div/div/div[2]/div[3]/button[2]")
        driver.execute_script("arguments[0].click();", element)
        # Add a brief pause to avoid rapid interactions
        time.sleep(4)  # Wait for 4 seconds before the next iteration
        # Refresh the page
        driver.refresh()
        time.sleep(5)

    time.sleep(4)

driver.quit()



