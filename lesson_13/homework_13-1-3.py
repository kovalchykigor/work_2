import xml.etree.ElementTree as ET
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def find_incoming_by_group_number(xml_file, group_number):
    # Завантаження XML файлу
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Пошук групи за номером
    for group in root.findall('group'):
        number = group.find('number').text
        if number == str(group_number):
            incoming = group.find('timingExbytes/incoming')
            if incoming is not None:
                logger.info(f'Incoming value for group number {group_number}: {incoming.text}')
            else:
                logger.info(f'No incoming value found for group number {group_number}')
            return

    logger.info(f'Group number {group_number} not found.')

# Виклик функції
find_incoming_by_group_number('groups.xml', 2)  # Замість 2 можна підставити потрібний номер групи
