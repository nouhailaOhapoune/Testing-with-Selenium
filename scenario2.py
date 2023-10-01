from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

from selenium.webdriver.support.wait import WebDriverWait

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
time.sleep(4)

# item in home page
element1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@id='editorjs']/div/div/div[11]/div/div/div/div[2]/a/span[2]")))
element1.click()
time.sleep(3)

# # Edit full form
# driver.find_element(By.XPATH, "//div[6]/div/div/div[3]/div/button").click()
# time.sleep(4)


# Read the CSV file
data = pd.read_csv("items_form.csv")

# Mapping CSV fields to their respective XPaths in the form
field_mapping = {
    'Item Code': ".frappe-control:nth-child(3) > .form-group .input-with-feedback",
    'Item Name': ".frappe-control:nth-child(4) > .form-group .input-with-feedback",
    'Item Group': ".frappe-control:nth-child(5) > .form-group .input-with-feedback",
    'Default Unit of Measure': ".frappe-control:nth-child(6) .input-with-feedback",
    'Opening Stock': ".frappe-control:nth-child(8) .input-with-feedback",
    'Standard Selling Rate': ".frappe-control:nth-child(9) .input-with-feedback"
}

i=0
# Loop through the rows in the DataFrame using indices
for i in range(len(data)):
    row = data.iloc[i]
    # Add item
    driver.find_element(By.XPATH, "//div[@id='page-List/Item/List']/div/div/div/div[2]/div[2]/button[2]/span").click()
    time.sleep(3)
    # Loop through the field mapping and fill out the form
    for field, css_selector in field_mapping.items():
        input_field = driver.find_element(By.CSS_SELECTOR, css_selector)
        input_field.clear()  # Clear the field
        input_field.send_keys(str(row[field]))
        time.sleep(2)

    # save the form
    wait = WebDriverWait(driver, 30)
    save_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-modal-primary")))
    driver.execute_script("arguments[0].click();", save_button)
    driver.refresh()
    time.sleep(5)

driver.quit()





