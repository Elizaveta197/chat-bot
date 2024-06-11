import logging
from .config import Config

config = Config.get_instance()

logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)

def get_logger(name):
    return logging.getLogger(name)
