from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def dynamic_keyboard(options):
    keyboard = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(text=opt, callback_data=f"choice_{idx}") for idx, opt in enumerate(options, start=1)]
    keyboard.add(*buttons)
    return keyboard

def pagination_keyboard(total_pages, current_page):
    keyboard = InlineKeyboardMarkup()
    if current_page > 1:
        keyboard.add(InlineKeyboardButton(text="<<", callback_data="prev_page"))
    if current_page < total_pages:
        keyboard.add(InlineKeyboardButton(text=">>", callback_data="next_page"))
    return keyboard

def confirmation_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    confirm_button = InlineKeyboardButton(text="Confirm", callback_data="confirm_yes")
    cancel_button = InlineKeyboardButton(text="Cancel", callback_data="confirm_no")
    keyboard.add(confirm_button, cancel_button)
    return keyboard
