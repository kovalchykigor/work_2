import pytest, requests

from .logger import logger
base_url = "http://127.0.0.1:8080/"


class TestFlaskServer:
    @pytest.mark.parametrize("sort_by, number", [
         pytest.param("brand", 2),
         pytest.param("year", 3),
         pytest.param("engine_volume", 4),
         pytest.param("price", 5),
         pytest.param("NOT_EXIST", 6, marks=pytest.mark.xfail),
         pytest.param("year", -1, marks=pytest.mark.xfail)
          ])
    def test_cars(self, auth_token, sort_by, number):
        logger.info(f"TEST DATA: Sort by = '{sort_by}' Limit = '{number}'")
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer ' + auth_token})
        response = session.get(f"{base_url}cars?sort_by={sort_by}&limit={number}")

        if response.status_code == 200:
            logger.info(f"REQUEST SUCCESS {response.status_code}")
        else:
            logger.error(f"REQUEST SUCCESS {response.status_code}")

        assert response.status_code == 200
