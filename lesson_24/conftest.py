from requests.auth import HTTPBasicAuth
import requests, pytest
from logger import logger


base_url = "http://127.0.0.1:8080/"
auth = "auth"

username = "test_user"
password = "test_pass"

# Налаштування логера


@pytest.fixture(scope="class")
def auth_token():
    logger.info("Authenticating user...")
    response = requests.post(base_url + auth, auth=HTTPBasicAuth(username, password))
    if response.status_code != 200:
        logger.error(f"Failed to authenticate: {response.status_code} - {response.text}")
        pytest.fail(f"Failed to authenticate: {response.status_code} - {response.text}")
    data = response.json()
    logger.info("Successfully authenticated")
    return data['access_token']

