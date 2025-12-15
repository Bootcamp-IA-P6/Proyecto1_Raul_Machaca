import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "taximeter.log")

def setup_logger():
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("taximeter")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
