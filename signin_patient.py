from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website = "https://vatb.mypainlog.ai/#/"
driver.get(website)
time.sleep(10)
driver.maximize_window()
print(driver.title)

driver.find_element(by="xpath", value="//input[@placeholder='Enter Your Email Address']").send_keys('vatbwebtest1@yopmail.com')
time.sleep(3)

driver.find_element(by="xpath", value="//input[@placeholder='Enter Your Password']").send_keys('Qweqwe1234@')
time.sleep(3)

driver.find_element(by="xpath", value="//button[normalize-space()='Sign in']").click()
time.sleep(15)      

driver.quit()