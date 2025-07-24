from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_buttons = ('1С',
                'Рекламации',
                'База знаний',
                'Сервисное обслуживание оборудования',
                'О компании',
                'Проверка вложенности',
                'Техническая поддержка')
def build_start_kb():
    builder = InlineKeyboardBuilder()
    for i, text in enumerate(menu_buttons):
        builder.button(text=text, callback_data=f'command_{i}')
    builder.adjust(1)
    return builder.as_markup()
