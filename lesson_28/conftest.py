import pytest
from selenium import webdriver
from .constants import LOGIN_URL


@pytest.fixture(scope="function")
def driver():
    return webdriver.Chrome()