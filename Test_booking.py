import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import re

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver2 = webdriver.Chrome()
    driver.get("https://www.booking.com/")
    driver2.get("https://temp-mail.org/en")
    yield {"driver1": driver, "driver2": driver2}
    driver.quit()
    driver2.quit()

def test_login_register(driver):
    time.sleep(30)
    driver1 = driver["driver1"]
    driver2 = driver["driver2"]
    time.sleep(4)
    
    temp_email = driver2.find_element(By.ID, "mail").get_attribute("value")
    
    driver1.find_element(By.XPATH, "//a[@aria-label='Sign in']").click()
    time.sleep(3)
    driver1.find_element(By.ID, "username").send_keys(temp_email)
    time.sleep(3)
    driver1.find_element(By.XPATH, "//button[@type='submit']").click()

    # input("👉 Please solve the CAPTCHA and press Enter to continue...")
        
    time.sleep(20)

    otp = driver2.find_element(By.XPATH, "//*[@id='tm-body']/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a").text[14:20]

    time.sleep(15)
    otp_inputs = driver1.find_elements(By.CSS_SELECTOR, "input[name^='code_']")

    for i in range(len(otp)):
        otp_inputs[i].send_keys(otp[i])    

    print(f'Temp email -> {temp_email}')
    print(f'OTP -> {otp}')

    time.sleep(3)
    driver1.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)

    assert driver1.current_url.startswith("https://www.booking.com/?auth_success=1"), \
        f"Login failed: unexpected URL {driver1.current_url}"




