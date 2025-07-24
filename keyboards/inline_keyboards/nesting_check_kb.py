from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.inline_keyboards.base_buttons import add_button_back, add_button_menu

nesting_check_buttons = ('Первый',
                         'Воторой',
                         'третий')


def build_nesting_check_kb():
    builder = InlineKeyboardBuilder()
    for i, text in enumerate(nesting_check_buttons):
        builder.button(text=text, callback_data=f'command_5_{i}')
    add_button_back(builder)
    add_button_menu(builder)
    builder.adjust(1)
    return builder.as_markup()


nesting_check_1_buttons = ('ПодПодКатегория',
                           '2 ПодПодКатегория')

def build_nesting_check_1_kb():
    builder = InlineKeyboardBuilder()
    for i, text in enumerate(nesting_check_1_buttons):
        builder.button(text=text, callback_data=f'command_5_0_{i}')
    add_button_back(builder)
    add_button_menu(builder)
    builder.adjust(1)
    return builder.as_markup()

nesting_check_2_buttons = ('Еще вложеннее',)
def build_nesting_check_2_kb():
    builder = InlineKeyboardBuilder()
    for i, text in enumerate(nesting_check_2_buttons):
        builder.button(text=text, callback_data=f'command_5_0_0_{i}')
    add_button_back(builder)
    add_button_menu(builder)
    builder.adjust(1)
    return builder.as_markup()
