from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver. get('chrome://settings/clearBrowserData')
button = driver.find_element(By.ID, "clearButton").click()


driver.get("https://staging.ezyslips.com/merchant.php")

# Find the username and password fields and input your credentials
username_field = driver.find_element(By.ID, 'username')  # Correctly indented
password_field = driver.find_element(By.ID, 'password')  # Also correctly indented


# Input credentials
username_field.send_keys('viraj.kumar+0101@shipway.com')
password_field.send_keys('Shipway@123')


# Submit the form (you can also find the submit button and click it)
password_field.send_keys(Keys.RETURN)

if "Dashboard" in driver.page_source:  # Adjust based on the page content after login
    print("Login successful!")
else:
    print("Login failed.")

driver.close()

