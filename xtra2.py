import re
import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def is_valid_email(email):
    # Regular expression for a simple email validation
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(email_pattern, email))

def wait_and_send_keys_with_validation(driver, by, value, keys, validation_func, wait_time=2):
    element = driver.find_element(by=by, value=value)
    time.sleep(wait_time)
    
    if validation_func(keys):
        element.send_keys(keys)
    else:
        raise ValueError("Invalid email format")

# Update the code to use the new function
def optimize_code():
    # ... (previous code)

    email = driver.find_element(by="xpath", value="//input[@id='emails']")
    wait_and_send_keys_with_validation(driver, "xpath", "//input[@id='emails']", 'stgwebtest103@yopmail.com', is_valid_email, 4)
    driver.execute_script("arguments[0].blur();", email)

    # ... (remaining code)
