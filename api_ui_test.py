from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Or use any other WebDriver like Firefox or Edge

# Test Case: Test registration form submission
def test_registration():
    driver.get("http://localhost:5000/")  # Open the home page
    time.sleep(2)  # Wait for 2 seconds for the page to load

    # Find form fields and fill them with test data
    full_name_input = driver.find_element_by_name("full_name")
    full_name_input.send_keys("John Doe")

    email_input = driver.find_element_by_name("email")
    email_input.send_keys("john.doe@example.com")

    phone_input = driver.find_element_by_name("phone_number")
    phone_input.send_keys("1234567890")

    # Similarly, fill other form fields...

    # Submit the form
    submit_button = driver.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()

    time.sleep(2)  # Wait for 2 seconds for the page to load

    # Verify if the success page is displayed
    assert "Success" in driver.title
    assert "Registration Successful" in driver.page_source

# Test Case: Test accessing the success page
def test_success_page():
    driver.get("http://localhost:5000/success")  # Open the success page
    time.sleep(2)  # Wait for 2 seconds for the page to load

    # Verify if the success page is displayed
    assert "Success" in driver.title
    assert "Registration Successful" in driver.page_source

# Close the WebDriver
driver.quit()
