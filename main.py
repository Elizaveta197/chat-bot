import asyncio
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from core.bot import TelegramBot
from core.config import Config
from db.database import Database
from utils.logger import get_logger

logger = get_logger(__name__)

async def on_startup(dispatcher):
    db = Database()
    await db.init_db()

    bot = TelegramBot()
    bot.register_handlers()

    logger.info("Приложение успешно запущено!")

async def on_shutdown(dispatcher):
    logger.info("Приложение останавливается...")

if __name__ == '__main__':
    Config.get_instance()

    storage = MemoryStorage()
    bot = TelegramBot()
    
    # Запуск поллинга сообщений
    executor.start_polling(bot.dispatcher, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True, storage=storage)
