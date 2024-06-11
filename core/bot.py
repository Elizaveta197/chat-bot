from aiogram import Bot, Dispatcher
from .config import Config

class TelegramBot:
    def __init__(self):
        self.config = Config.get_instance()
        self.bot = Bot(token=self.config.TELEGRAM_API_TOKEN)
        self.dispatcher = Dispatcher(self.bot)

    async def start_polling(self):
        await self.dispatcher.start_polling()

    def register_handlers(self):
        from .handlers import register_all_handlers
        register_all_handlers(self.dispatcher)
