from .config import Config
from .bot import TelegramBot
from .database import Database
from .logging import get_logger

config = Config.get_instance()

logger = get_logger(__name__)

database = Database()

bot = TelegramBot()

async def initialize_core_components():
    logger.info("Initializing database...")
    await database.init_db()

    logger.info("Registering bot handlers...")
    bot.register_handlers()

    logger.info("Core components initialized successfully.")
