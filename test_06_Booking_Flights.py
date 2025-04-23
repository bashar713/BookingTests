import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta

@pytest.fixture
def booking_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_flight_search(booking_driver):
    driver = booking_driver
    wait = WebDriverWait(driver, 20)

    # 1) Navigate & open Flights tab
    driver.get("https://booking.kayak.com/")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//a[contains(@class,'UIM7-product') and normalize-space(.)='Flights']")
    )).click()

    # 2) Clear any existing origin
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//div[contains(@class,'c_neb-item-close')]//div[@role='button']")
    )).click()

    # 3) Enter origin → select first suggestion
    origin = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//input[@aria-label='Flight origin input']")
    ))
    origin.clear()
    origin.send_keys("Tel Aviv")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "(//li[@role='option'])[1]")
    )).click()

    # 4) Enter destination → select first suggestion
    dest = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//input[@data-test-destination]")
    ))
    dest.clear()
    dest.send_keys("Paris")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "(//li[@role='option'])[1]")
    )).click()

    # 5) Compute dynamic dates (7 days out, 2-day return)
    today          = date.today()
    depart_date    = today + timedelta(days=7)
    return_date    = depart_date + timedelta(days=2)
    # labels must match the beginning of the aria-label on each date-button
    depart_label   = depart_date.strftime("%B") + " " + str(depart_date.day) + ", " + str(depart_date.year)
    return_label   = return_date.strftime("%B") + " " + str(return_date.day) + ", " + str(return_date.year)

    # 6) Open the Departure calendar
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//div[@aria-label='Departure']")
    )).click()
    # 7) Click the computed departure date
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         f"//td[@role='gridcell']//div[@role='button' and contains(@aria-label, '{depart_label}')]")
    )).click()

    # 8) Open the Return calendar
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//div[@aria-label='Return']")
    )).click()
    # 9) Click the computed return date
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         f"//td[@role='gridcell']//div[@role='button' and contains(@aria-label, '{return_label}')]")
    )).click()

    # 10) Click Search
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//button[@aria-label='Search']")
    )).click()

    # 11) Wait for the results container (stable, non-changing ID)
    results = wait.until(EC.visibility_of_element_located(
        (By.XPATH,
         "//div[@id='flight-results-list-wrapper']")
    ))
    assert results.is_displayed(), "Flight results did not load"
