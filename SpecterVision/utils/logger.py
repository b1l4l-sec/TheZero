import os
import logging
from datetime import datetime
from config.settings import LOGS_DIR

def setup_logger(name='spectervision'):
    os.makedirs(LOGS_DIR, exist_ok=True)

    log_filename = os.path.join(
        LOGS_DIR,
        f"{name}_{datetime.now().strftime('%Y%m%d')}.log"
    )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger

logger = setup_logger()
