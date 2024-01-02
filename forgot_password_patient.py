from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website = "https://stg.injurycloud.com"
driver.get(website)
# time.sleep(5)
driver.maximize_window()
time.sleep(2)

driver.find_element(by="xpath", value="//div[@class='signin-forgot-password']").click()
time.sleep(3)

driver.find_element(by="xpath", value="//input[@id='Email']").send_keys('stgwebtest1@yopmail.com')

driver.find_element(by="xpath", value="//button[@id='submit-btn']").click()

driver.find_element(by="xpath", value="//button[normalize-space()='Ok']").click()

