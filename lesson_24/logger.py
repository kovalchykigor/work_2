
import logging

# Створення логера

logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('test_search.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


# Логування подій
logger.debug('Це повідомлення рівня DEBUG')
logger.info('Це повідомлення рівня INFO')
logger.warning('Це повідомлення рівня WARNING')
logger.error('Це повідомлення рівня ERROR')
logger.critical('Це повідомлення рівня CRITICAL')