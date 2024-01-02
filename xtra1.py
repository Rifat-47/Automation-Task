from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website = "https://stg.injurycloud.com"
driver.get(website)
driver.maximize_window()

max_wait_time = 15
counter = 1

try:
    while counter <= max_wait_time:
        try:
            # Use WebDriverWait to wait until the element is present in the DOM
            element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Terms of Service']"))
            )

            # If the element is found, break out of the loop
            break

        except Exception as e:
            # Sleep for 1 second before checking again
            time.sleep(1)
            # Increment the counter
            counter += 1

    # Now, you can work with the element
    # For example, click on it
    element.click()

except Exception as e:
    print(f"Element not found within {max_wait_time} seconds. Error: {e}")

finally:
    # Print the number of times the element was checked
    print(f"Element found after {counter} seconds.")
    time.sleep(15)
    driver.quit()
