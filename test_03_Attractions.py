import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def booking_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Initialize Chrome only once, with options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.booking.com/")
    
    yield driver
    driver.quit()

def test_attractions_search(booking_driver):
    wait = WebDriverWait(booking_driver, 20) 

    experiences_link = wait.until(EC.element_to_be_clickable((By.ID, "attractions")))
    experiences_link.click()    

    heading_element = WebDriverWait(booking_driver, 20).until(
        EC.presence_of_element_located((
            By.XPATH, "//h1[contains(text(), 'Attractions, activities, and experiences')]"
        ))
    )

    assert "Attractions, activities, and experiences" in heading_element.text, \
        f"Error: Expected heading not found. Got: {heading_element.text}"

    destination_input = wait.until(EC.element_to_be_clickable((By.NAME, "query")))
    destination_input.clear()
    destination_input.send_keys("Paris")

    time.sleep(3)

    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='search-button']")))
    assert search_button.is_enabled(), "Error: Search button is not enabled or clickable."
    search_button.click()

    time.sleep(2)
    search_button.click()

    result_element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Paris attractions')]")
    ))

    assert "Paris" in result_element.text and "attraction" in result_element.text, \
        f"Unexpected result heading: {result_element.text}"
