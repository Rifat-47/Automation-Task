from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website = "https://stg.mypainlog.ai/#/"
driver.get(website)
time.sleep(5)
driver.maximize_window()
time.sleep(2)
print(driver.title)

driver.find_element(by="xpath", value="//input[@placeholder='Enter Your Email Address']").send_keys('stgwebtest1@yopmail.com')
time.sleep(2)

driver.find_element(by="xpath", value="//input[@placeholder='Enter Your Password']").send_keys('Qweqwe1234@')
time.sleep(2)

driver.find_element(by="xpath", value="//button[normalize-space()='Sign in']").click()
time.sleep(12)      

driver.quit()