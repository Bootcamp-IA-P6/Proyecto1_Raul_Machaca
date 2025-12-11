import logging
import os

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "taximeter.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("taximeter_logger")
