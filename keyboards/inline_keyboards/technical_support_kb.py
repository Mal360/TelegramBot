from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.inline_keyboards.base_buttons import add_button_back, add_button_menu

technical_support_buttons = ()


def build_technical_support_kb():
    builder = InlineKeyboardBuilder()
    for i, text in enumerate(technical_support_buttons):
        builder.button(text=text, callback_data=f'command_6_{i}')
    add_button_back(builder)
    add_button_menu(builder)
    builder.adjust(1)
    return builder.as_markup()
