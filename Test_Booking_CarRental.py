import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_car_rental_search_flow(driver):
    wait = WebDriverWait(driver, 40)

    # 1) Go to Booking.com
    driver.get("https://www.booking.com")

    # 2) Click “Car rentals”
    wait.until(EC.element_to_be_clickable((By.ID, "cars"))).click()

    # 3) Enter “London” into the pickup-location field
    pickup = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//input[@name='pickup-location' and contains(@class,'SearchBoxFieldAutocomplete_input')]"
    )))
    pickup.clear()
    pickup.send_keys("London")

    # 4) Wait for the dropdown listbox
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='listbox']")))

    # 5) Click the first suggestion:
    #    - select the first <div> child under role="listbox"
    #    - then click its <button>
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "(//div[@role='listbox']/div)[1]//button"
    ))).click()

    # 6) Click “Search”
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//span[contains(@class,'LPCM_b7bff305')]"
    ))).click()

    # 7) Verify the results header appears (any <h1> whose class starts with "SM_")
    result_header = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//h1[starts-with(@class,'SM_')]"
    )))
    assert result_header.is_displayed()
