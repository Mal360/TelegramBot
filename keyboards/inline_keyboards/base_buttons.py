from aiogram.utils.keyboard import InlineKeyboardBuilder


def add_button_back(builder):
    builder.button(text='<< Назад', callback_data='back')


def add_button_menu(builder):
    builder.button(text='В меню ↩', callback_data='menu')


def build_button_back():
    builder = InlineKeyboardBuilder()
    add_button_back(builder)


def build_button_menu():
    builder = InlineKeyboardBuilder()
    add_button_menu(builder)
    return builder.as_markup()


def build_buttons_back_menu():
    builder = InlineKeyboardBuilder()
    add_button_back(builder)
    add_button_menu(builder)
    return builder.as_markup()
