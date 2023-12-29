from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website = "https://vatb.mypainlog.ai/#/sign-up"
driver.get(website)
time.sleep(10)
driver.maximize_window()
print(driver.title)

email = driver.find_element(by='xpath', value="//input[@placeholder='Enter your email address']")
email.send_keys('vatbwebtest103@yopmail.com')
driver.execute_script("arguments[0].blur();", email)
time.sleep(10)

try: 
    check_registered_user = driver.find_element(by='xpath', value = "//div[@class='alert-text error-message']")
    time.sleep(3)
    print(check_registered_user)
    if check_registered_user:
        print("User already registered")

except:
        # driver.find_element(by='xpath', value = "//input[@placeholder='Enter your first name']").send_keys('')
        # time.sleep(1)
        # driver.find_element(by='xpath', value = "//input[@placeholder='Enter your last name']").send_keys('')
        time.sleep(1)
        driver.find_element(by='xpath', value = "//input[@placeholder='Feet']").send_keys(5)
        time.sleep(3)
        driver.find_element(by='xpath', value = "//input[@placeholder='Inch']").send_keys(9)
        time.sleep(3)
        driver.find_element(by='xpath', value = "//input[@placeholder='Enter your Weight(LBS)']").send_keys(149)
        time.sleep(3)
        gender = driver.find_element(by='xpath', value = "//select[@name='Gender']")
        gender_options = Select(gender)
        gender_options.select_by_visible_text("Male")
        time.sleep(3)

        hand = driver.find_element(by='xpath', value = "//select[@name='DominantHand']")
        hand_options = Select(hand)
        hand_options.select_by_visible_text("Left")

        driver.find_element(by='xpath', value = "//input[@placeholder='Enter your Password']").send_keys('Qweqwe1234@')
        time.sleep(3)

        driver.find_element(by='xpath', value = "//input[@placeholder='Enter your confirmed password']").send_keys('Qweqwe1234@')
        time.sleep(3)

        driver.find_element(by='xpath', value = "//label[@class='kt-checkbox kt-checkbox--brand']/span").click()
        time.sleep(3)

        driver.find_element(by='xpath', value = "//button[normalize-space()='Sign up']").click()
        time.sleep(15)

driver.quit()


