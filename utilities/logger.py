import logging
import os
from datetime import datetime

def get_logger(name):

    # Create logs folder if not exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Create log file with timestamp
    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
    log_path = os.path.join("logs", log_filename)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:
        file_handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


