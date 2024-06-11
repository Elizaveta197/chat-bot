import os
from functools import lru_cache

class Config:
    TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
    DATABASE_URL = os.getenv('DATABASE_URL')
    AI_MODEL_PATH = os.getenv('AI_MODEL_PATH')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @staticmethod
    @lru_cache()
    def get_instance():
        return Config()
