from aiogram import types

async def process_callback_query(query: types.CallbackQuery):
    await query.answer("Ваш запрос обрабатывается...")
    await query.message.edit_text("Запрос обработан. Спасибо за ожидание.")

