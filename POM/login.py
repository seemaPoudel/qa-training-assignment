from selenium import webdriver
from loginpage import LoginPage
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


# create page object
login_page = LoginPage(driver)

# use page method instead of writing locator again
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login()
time.sleep(3)

# Validate login by checking API
assert "inventory" in driver.current_url
print("Login Test Passed!!")

driver.quit()
