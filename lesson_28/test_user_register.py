import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from .constants import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(LOGIN_URL)

    def click_on(self, locator):
        element = WebDriverWait(self.driver, timeout=3).until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, data):
        element = WebDriverWait(self.driver, timeout=3).until(EC.presence_of_element_located(locator))
        element.send_keys(data)


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def make_registration_data(self):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        return first_name, last_name, email, password

    def fill_registration_form(self):
        first_name, last_name, email, password = self.make_registration_data()
        self.send_keys(INPUT_NAME, first_name)
        self.send_keys(INPUT_LAST_NAME, last_name)
        self.send_keys(INPUT_EMAIL, email)
        self.send_keys(INPUT_PASSWORD, password)
        self.send_keys(INPUT_PASSWORD_AGAIN, password)


def generate_test_data():
    """
    Generates four sets of test data:
    1. with an empty first_name
    2. with an empty last_name
    3. with an empty email
    4. with an empty password
    """
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()

    return [
        {"first_name": "", "last_name": last_name, "email": email, "password": password},
        {"first_name": first_name, "last_name": "", "email": email, "password": password},
        {"first_name": first_name, "last_name": last_name, "email": "", "password": password},
        {"first_name": first_name, "last_name": last_name, "email": email, "password": ""}
    ]


class TestUserRegisterPositive:
    def test_user_register(self, driver):
        start_page = StartPage(driver)
        start_page.open()
        start_page.click_on(SIGN_IN)
        start_page.click_on(LINK_REGISTRATION)

        start_page.fill_registration_form()
        start_page.click_on(BUTTON_REGISTER)
        time.sleep(2)


class TestUserRegisterNegative:
    @pytest.mark.xfail
    @pytest.mark.parametrize('data', generate_test_data())
    def test_with_out_one_field(self, driver, data):
        start_page = StartPage(driver)
        start_page.open()
        start_page.click_on(SIGN_IN)
        start_page.click_on(LINK_REGISTRATION)

        # Extract data from the parameter
        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]

        start_page.send_keys(INPUT_NAME, first_name)
        start_page.send_keys(INPUT_LAST_NAME, last_name)
        start_page.send_keys(INPUT_EMAIL, email)

        start_page.send_keys(INPUT_PASSWORD, password)
        start_page.send_keys(INPUT_PASSWORD_AGAIN, password)

        start_page.click_on(BUTTON_REGISTER)

        time.sleep(2)
