from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class connexion():
    driver = webdriver.Chrome()
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