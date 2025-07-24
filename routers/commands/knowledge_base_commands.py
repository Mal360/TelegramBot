from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.base_buttons import build_button_menu
from keyboards.inline_keyboards.knowledge_base_kb import build_knowledge_base_kb, knowledge_base_buttons
from routers.commands.base_commands import text_doc_to_study, wait

router = Router(name=__name__)


@router.callback_query(F.data == 'command_2')
async def handle_knowledge_base(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите подкатегорию', reply_markup=build_knowledge_base_kb())


@router.callback_query(F.data == 'command_2_0')
async def handle_2_0(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text=text_doc_to_study + knowledge_base_buttons[0], reply_markup=build_button_menu())
    file_path = '../../media/media_knowledge_base/Барный инвентарь.pdf'


@router.callback_query(F.data == 'command_2_1')
async def handle_2_0(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text=text_doc_to_study + knowledge_base_buttons[1], reply_markup=build_button_menu())
    file_path = '../../media/media_knowledge_base/Сиропы, топинги, пюре.pdf'


@router.callback_query(F.data == 'command_2_2')
async def handle_2_0(callback: CallbackQuery):
    await wait(callback.message)
