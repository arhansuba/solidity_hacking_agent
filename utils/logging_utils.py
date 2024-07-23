# logging_utils.py

import logging

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """
    Set up a logger.
    """
    logger = logging.getLogger(name)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

def log_info(logger: logging.Logger, message: str) -> None:
    """
    Log an info message.
    """
    logger.info(message)

def log_error(logger: logging.Logger, message: str) -> None:
    """
    Log an error message.
    """
    logger.error(message)
