# import time
#
# import psycopg2
# import pytest
# from time import sleep
#
# @pytest.fixture(scope="session")
# def create_table():
#     time.sleep(1)
#     conn = psycopg2.connect("postgresql://postgres:postgres@db:5432/postgres")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE users (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(100),
#             age INT
#         );
#     """)
#     conn.commit()
#     cursor.close()
#     conn.close()
#     yield