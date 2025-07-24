from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.inline_keyboards.base_buttons import add_button_back, add_button_menu

knowledge_base_buttons = ('Барный инвентарь',
                 'Сиропы, топинги, пюре',
                 'Оборудование')


def build_knowledge_base_kb():
    builder = InlineKeyboardBuilder()
    for i, text in enumerate(knowledge_base_buttons):
        builder.button(text=text, callback_data=f'command_2_{i}')
    add_button_back(builder)
    add_button_menu(builder)
    builder.adjust(1)
    return builder.as_markup()
