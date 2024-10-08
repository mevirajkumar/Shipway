import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



driver = selenium.webdriver.Chrome()
driver.maximize_window()
driver.get("https://staging.ezyslips.com/register_new")

button = WebDriverWait(driver, 2)


# Fill out the registration form
name_field = driver.find_element(By.ID, 'company_admin_firstname') #finding element name
name_field.send_keys('TESTNAME1') # Passing 'value'


company_name_field = driver.find_element(By.ID, 'company_description_company') #finding element company name
company_name_field.send_keys('TESTNAME1') # Passing 'value'


email_field = driver.find_element(By.ID, 'company_description_email') #finding element email
email_field.send_keys('TESTNAME1') # Passing 'value'

number_field = driver.find_element(By.ID, 'jquery-intl-phone') #finding element mobile no
number_field.send_keys('1234') # Passing 'value'

password_field = driver.find_element(By.ID, 'company_description_password')  # finding element password
password_field.send_keys('Test@1234')  # Passing 'value'



order_volume_field = driver.find_element(By.ID, 'no_of_shipments')  # finding element password

dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'no_of_shipments'))
)

# Create a Select object from the dropdown
select = Select(dropdown)  # Make sure there's no extra indentation here

# Select an option by visible text
select.select_by_visible_text('0 - 100')

# Print the selected option
selected_option = select.first_selected_option

#close browser
driver.close()

