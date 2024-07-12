import json
import logging
import os

# Налаштування логування
logging.basicConfig(filename='json__result.log', level=logging.ERROR)
logger = logging.getLogger(__name__)

def validate_json_files(file_paths):
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json.load(f)  # Спроба завантажити JSON
            print(f"{file_path} is valid JSON.")
        except json.JSONDecodeError as e:
            logger.error(f'Invalid JSON in {file_path}: {e}')
            print(f"{file_path} is not valid JSON. Check the log for details.")

# Список файлів для валідації
json_files = [
    'localizations_en.json',
    'localizations_ru.json',
    'login.json',
    'swagger.json'
]

validate_json_files(json_files)
