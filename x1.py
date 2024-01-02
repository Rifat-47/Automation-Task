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

driver.find_element(by="xpath", value="//input[@id='Email']").send_keys('rtaher@mymedicalhub.com')
time.sleep(2)

driver.find_element(by="xpath", value="//input[@id='Password']").send_keys('QWEqwe1234@')
time.sleep(2)

driver.find_element(by="xpath", value="//button[@id='login-btn']").click()
time.sleep(7)

driver.find_element(by="xpath", value="//a[normalize-space()='Invite a Patient']").click()
time.sleep(2)

driver.find_element(by="xpath", value="//label[normalize-space()='Self Assessment']").click()
time.sleep(2)

driver.find_element(by="xpath", value="//div[@id='msk-region']//div[5]").click()
time.sleep(2)

email = driver.find_element(by="xpath", value="//input[@id='emails']")
email.send_keys('stgwebtest103@yopmail.com')
driver.execute_script("arguments[0].blur();", email)
time.sleep(4)

firstName = driver.find_element(by='xpath', value="//input[@id='FirstName_R']")
print(firstName.get_attribute('value'))
if not firstName.get_attribute('value'):
    firstName.send_keys('stgweb')
    time.sleep(2)

lastName = driver.find_element(by="xpath", value="//input[@id='LastName_R']")
print(lastName.get_attribute('value'))
if not lastName.get_attribute('value'):
    lastName.send_keys('test1')
    time.sleep(2)

driver.find_element(by="xpath", value="//button[@id='refersendrefermodalbtn']").click()
time.sleep(13)

driver.quit()