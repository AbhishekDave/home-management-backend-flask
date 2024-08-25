# src/utils/configure_logging.py

import logging
from logging.handlers import RotatingFileHandler
import json
import os


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'time': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
        }
        return json.dumps(log_record)


def configure_logging(app):
    """
    Configures logging for the Flask application.

    Logs are output to both the console and separate files for each log level.
    """

    # Create base log directory
    base_log_dir = 'logs'
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']

    # Create subdirectories for each log level
    for level in log_levels:
        log_dir = os.path.join(base_log_dir, level)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    # File paths for each log level
    log_file_paths = {
        'debug': os.path.join(base_log_dir, 'debug', 'app.log'),
        'info': os.path.join(base_log_dir, 'info', 'app.log'),
        'warning': os.path.join(base_log_dir, 'warning', 'app.log'),
        'error': os.path.join(base_log_dir, 'error', 'app.log'),
        'critical': os.path.join(base_log_dir, 'critical', 'app.log')
    }

    # Set up logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Capture all log levels in the console
    console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)

    # Set up file handlers with rotation
    handlers = {
        'DEBUG': RotatingFileHandler(log_file_paths['debug'], maxBytes=10000000, backupCount=5),
        'INFO': RotatingFileHandler(log_file_paths['info'], maxBytes=10000000, backupCount=5),
        'WARNING': RotatingFileHandler(log_file_paths['warning'], maxBytes=10000000, backupCount=5),
        'ERROR': RotatingFileHandler(log_file_paths['error'], maxBytes=10000000, backupCount=5),
        'CRITICAL': RotatingFileHandler(log_file_paths['critical'], maxBytes=10000000, backupCount=5),
    }

    # Set log levels and formatters for file handlers
    for level, handler in handlers.items():
        handler.setLevel(getattr(logging, level))  # Set handler level
        handler.setFormatter(JsonFormatter())  # JSON formatter for structured logging
        app.logger.addHandler(handler)  # Add each handler to the app's logger

    # Set up the app's logger level to DEBUG to capture all levels
    app.logger.setLevel(logging.DEBUG)

    # Add console handler (if desired) to log to console
    app.logger.addHandler(console_handler)
