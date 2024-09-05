from selenium import webdriver
from . import Url

import pytest


@pytest.fixture(scope="function")
def driver():
    return webdriver.Chrome()


@pytest.fixture(scope="function")
def url():
    return Url.url