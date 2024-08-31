import logging

# Створення логера
logger = logging.getLogger("test_logger")
logger.setLevel(logging.DEBUG)

# Створення обробника для логування у файл
file_handler = logging.FileHandler("test_search.log")
file_handler.setLevel(logging.DEBUG)

# Створення обробника для логування у консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Форматування логів
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Додавання обробників до логера
logger.addHandler(file_handler)
logger.addHandler(console_handler)
