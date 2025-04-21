import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import re
import random
import string

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver2 = webdriver.Chrome()
#     driver.get("https://www.booking.com/")
#     driver2.get("https://temp-mail.org/en")
#     yield {"driver1": driver, "driver2": driver2}
#     driver.quit()
#     driver2.quit()

@pytest.fixture
def booking_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.booking.com/")
    yield driver
    driver.quit()
    
# def test_login_register(driver):
#     driver1 = driver["driver1"]
#     driver2 = driver["driver2"]

#     wait1 = WebDriverWait(driver1, 40)
#     wait2 = WebDriverWait(driver2, 40)


#     def email_is_ready(driver):
#         email = driver.find_element(By.ID, "mail").get_attribute("value")
#         return email if "@" in email else False

#     temp_email = wait2.until(email_is_ready)


#     sign_in_button = wait1.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Sign in']")))
#     sign_in_button.click()

#     username_field = wait1.until(EC.presence_of_element_located((By.ID, "username")))
#     username_field.send_keys(temp_email)

#     submit_button = wait1.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#     submit_button.click()

#     # input("👉 Please solve the CAPTCHA and press Enter to continue...")

#     otp_element = wait2.until(EC.presence_of_element_located((
#         By.XPATH,
#         "//*[@id='tm-body']/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a"
#     )))
#     otp = otp_element.text[14:20]

#     assert otp and len(otp) == 6, f"❌ OTP not received or invalid: '{otp}'"

#     otp_inputs = wait1.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[name^='code_']")))


#     for i in range(len(otp)):
#         otp_inputs[i].send_keys(otp[i])

#     print(f'Temp email -> {temp_email}')
#     print(f'OTP -> {otp}')

#     otp_submit = wait1.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#     otp_submit.click()

#     wait1.until(EC.url_contains("auth_success=1"))

#     assert driver1.current_url.startswith("https://www.booking.com/?auth_success=1"), \
#         f"Login failed: unexpected URL {driver1.current_url}"


# def test_login_error(booking_driver):
#     wait1 = WebDriverWait(booking_driver, 20)

#     sign_in_button = wait1.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Sign in']")))
#     sign_in_button.click()

#     username_field = wait1.until(EC.presence_of_element_located((By.ID, "username")))
#     username_field.send_keys("test@gmail.com")

#     submit_button = wait1.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#     submit_button.click()

#     time.sleep(10)

#     for _ in range(3):  
#         otp_inputs = wait1.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[name^='code_']")))

#         wrong_otp = ''.join(random.choices(string.digits, k=6))

#         for i in range(6):
#             otp_inputs[i].clear()
#             otp_inputs[i].send_keys(wrong_otp[i])

#         otp_submit = wait1.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#         otp_submit.click()
#         time.sleep(2)

#     try:
#         error_message = wait1.until(EC.presence_of_element_located((By.XPATH, "//span[@class='error-block']")))
#         assert "Too many failed attempts" in error_message.text
#         print("❗ Error message found:", error_message.text)
#     except:
#         print("❌ Error message not found.")


def test_print(booking_driver):
    print("Hello")