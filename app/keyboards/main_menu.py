from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Добавить товар"),
        ],
        [
            KeyboardButton(text="📋 Список покупок"),
        ],
        [
            KeyboardButton(text="📂 Категории"),
        ],
    ],
    resize_keyboard=True,
)