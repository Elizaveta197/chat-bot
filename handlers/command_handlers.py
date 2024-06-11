from aiogram import types

async def start_command(message: types.Message):
    await message.reply("Чат-бот активирован. Введите ваш запрос.")

async def help_command(message: types.Message):
    await message.reply("Список доступных команд: /start, /help, /status")

async def status_command(message: types.Message):
    await message.reply("Система в нормальном состоянии. Все системы функционируют.")

