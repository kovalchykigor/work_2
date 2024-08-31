import time
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..lesson_27 import Url, ParcelCode, Locators

@pytest.mark.parametrize("parcel_number, expected_message",
                             [
                                 pytest.param("11111111111111", "Отримано", marks=pytest.mark.xfail),
                                 pytest.param(ParcelCode.parcel_code, "Отримано")

                             ])
def test_np(parcel_number, expected_message):
    driver = webdriver.Chrome()

    driver.get(Url.url)
    tracking_field = WebDriverWait(driver, timeout=2).until(
        EC.presence_of_element_located((By.ID, Locators.input_field))
    )
    tracking_field.send_keys(parcel_number)

    button_search = WebDriverWait(driver, timeout=2).until(
        EC.presence_of_element_located((By.ID, Locators.button_find))
    )
    button_search.click()

    button_ok = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, Locators.pop_up_button)))
    button_ok.click()
    time.sleep(3)

    parcel_status = driver.find_element(By.CSS_SELECTOR, Locators.parcel_status)
    assert expected_message in parcel_status.text, f"NO '{expected_message}' in received message"

