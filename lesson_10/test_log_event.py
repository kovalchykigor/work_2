import pytest
import logging
from unittest.mock import patch
from .homework_10 import log_event


class MockLogger:
    def __init__(self):
        self.messages = {'info': [], 'warning': [], 'error': []}

    def info(self, message):
        self.messages['info'].append(message)

    def warning(self, message):
        self.messages['warning'].append(message)

    def error(self, message):
        self.messages['error'].append(message)


def test_log_event_success():
    mock_logger = MockLogger()

    with patch('logging.getLogger', return_value=mock_logger):
        log_event('test_user', 'success')

    assert mock_logger.messages['info'] == ['Login event - Username: test_user, Status: success']
    assert mock_logger.messages['warning'] == []
    assert mock_logger.messages['error'] == []


def test_log_event_expired():
    mock_logger = MockLogger()

    with patch('logging.getLogger', return_value=mock_logger):
        log_event('test_user', 'expired')

    assert mock_logger.messages['info'] == []
    assert mock_logger.messages['warning'] == ['Login event - Username: test_user, Status: expired']
    assert mock_logger.messages['error'] == []


def test_log_event_failed():
    mock_logger = MockLogger()

    with patch('logging.getLogger', return_value=mock_logger):
        log_event('test_user', 'failed')

    assert mock_logger.messages['info'] == []
    assert mock_logger.messages['warning'] == []
    assert mock_logger.messages['error'] == ['Login event - Username: test_user, Status: failed']


def test_log_event_invalid_status():
    mock_logger = MockLogger()

    with patch('logging.getLogger', return_value=mock_logger):
        log_event('test_user', 'invalid_status')

    assert mock_logger.messages['info'] == []
    assert mock_logger.messages['warning'] == []
    assert mock_logger.messages['error'] == ['Login event - Username: test_user, Status: invalid_status']
