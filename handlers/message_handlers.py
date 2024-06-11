from aiogram import types
import random

async def echo_message(message: types.Message):
    response_variations = ["Интересный вопрос...", "Подумайте еще раз.", "Не могу сейчас ответить.", "Может быть, попробуем другой вопрос?"]
    await message.answer(random.choice(response_variations))

async def analyze_message(message: types.Message):
    analysis_result = "Это очень сложный запрос, над которым нужно подумать."
    await message.reply(analysis_result)

