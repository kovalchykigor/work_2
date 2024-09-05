import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..lesson_27 import Url, ParcelCode, Locators


class BasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def button_click(self, By, locator):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable((By, locator))
        )
        element.click()

    def send_keys(self, By, locator, data):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located((By, locator))
        )
        element.send_keys(data)


class NPSearchPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver=driver, url=url)

    def get_search_message(self, By, locator):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located((By, locator))
        )
        return element.text



class TestNP:
    @pytest.mark.parametrize("parcel_number, expected_message",
                                 [
                                     pytest.param("11111111111111", "Отримано", marks=pytest.mark.xfail),
                                     pytest.param(ParcelCode.parcel_code, "Отримано")

                                 ])
    def test_np(self, driver, url, parcel_number, expected_message):
        np_search_page = NPSearchPage(driver, url)
        np_search_page.open()

        np_search_page.send_keys(By.ID, Locators.input_field, parcel_number)

        np_search_page.button_click(By.ID, Locators.button_find)

        np_search_page.button_click(By.CSS_SELECTOR, Locators.pop_up_button)

        actual_message = np_search_page.get_search_message(By.CSS_SELECTOR, Locators.parcel_status)
        assert expected_message in actual_message, f"Expected message '{expected_message}' != actual message '{actual_message}'"





