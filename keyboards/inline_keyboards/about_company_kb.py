from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.inline_keyboards.base_buttons import add_button_back, add_button_menu

about_company_buttons = ()


def build_about_company_kb():
    builder = InlineKeyboardBuilder()
    for i, text in enumerate(about_company_buttons):
        builder.button(text=text, callback_data=f'command_4_{i}')
    add_button_back(builder)
    add_button_menu(builder)
    builder.adjust(1)
    return builder.as_markup()
