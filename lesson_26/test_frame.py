import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

url = "http://localhost:8000/dz.html"


class Assertion:
    def assert_expected_message(self, actual_message, expected_message):
        assert actual_message == expected_message, f"Actual message '{actual_message}'!= expected message '{expected_message}'"


class TestFrame:
    @pytest.mark.parametrize("frame, fraze, expected_message",
                             [
                                 pytest.param("frame1", "Frame1_Secret", "Верифікація пройшла успішно!"),
                                 pytest.param("frame2", "Frame2_Secret", "Верифікація пройшла успішно!"),
                                 pytest.param("frame1", "Wrong_text1", "Введено неправильний текст!"),
                                 pytest.param("frame2", "Wrong_text2", "Введено неправильний текст!")
                             ])
    def test_frame(self, driver, frame, fraze, expected_message ):
        driver.get(url)

        driver.switch_to.frame(driver.find_element(By.ID, frame))
        input1 = driver.find_element(By.TAG_NAME, "Input")
        input1.send_keys(fraze)
        time.sleep(1)

        verifyInput = driver.find_element(By.TAG_NAME, "button")
        verifyInput.click()

        alert = Alert(driver)
        alert_message = alert.text

        assertion = Assertion()
        assertion.assert_expected_message(alert_message, expected_message)
        time.sleep(1)