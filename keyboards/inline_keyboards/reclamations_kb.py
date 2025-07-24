from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.inline_keyboards.base_buttons import add_button_back, add_button_menu

reclamations_buttons = ('Клён',
                 'Рестинтернешнл',
                 'Мастергласс',
                 'Регион 50 (Проект 2015)',
                 'Русский проект (Метроном)')


def build_reclamations_kb():
    builder = InlineKeyboardBuilder()
    for i, text in enumerate(reclamations_buttons):
        builder.button(text=text, callback_data=f'command_1_{i}')
    add_button_back(builder)
    add_button_menu(builder)
    builder.adjust(1)
    return builder.as_markup()
