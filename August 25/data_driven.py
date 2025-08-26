from selenium import webdriver
from selenium.webdriver.common.by import By
import csv, time

# launch browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# read test data
with open("testdata.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # login
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(row["username"])
        driver.find_element(By.ID, "password").send_keys(row["password"])
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        # logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)

# close browser
driver.quit()