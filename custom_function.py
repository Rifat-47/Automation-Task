from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

max_wait_time = 15
def find_and_send_key(driver, by, value, wait=1, element_name=any):
	counter = 1
	try:
		while counter <= max_wait_time:
			try:
				if by.upper() == 'XPATH':
					element = WebDriverWait(driver, 1).until(
						EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Terms of Service']"))
					).send_keys(value)
					time.sleep(wait)
					break
			except Exception as e:
				time.sleep(1)
				counter += 1

	except Exception as e:
		print(f"{element_name} not found within {max_wait_time} seconds. Error: {e}")
    
	finally:
	    print(f"{element_name} found after {counter} seconds.")