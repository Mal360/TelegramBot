from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaDocument

from keyboards.inline_keyboards.base_buttons import build_button_menu
from keyboards.inline_keyboards.one_c_kb import build_one_c_kb, one_c_buttons
from routers.commands.base_commands import text_doc_to_study, wait

router = Router(name=__name__)


@router.callback_query(F.data == 'command_0')
async def handle_one_c(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите подкатегорию', reply_markup=build_one_c_kb())


@router.callback_query(F.data == 'command_0_0')
async def handle_0_0(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text=text_doc_to_study + one_c_buttons[0],
                                     reply_markup=build_button_menu())
    file_path = '../../media/media_one_c/Создание_Заказа_Покупателя_и_выставление_счёта.pdf'
    # await callback.message.reply_document(document=FSInputFile(path=file_path))
    # await callback.message.edit_media(media=InputMediaDocument(media=file_path))


@router.callback_query(F.data == 'command_0_1')
async def handle_0_1(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text=text_doc_to_study + one_c_buttons[1],
                                     reply_markup=build_button_menu())
    file_path = '../../media/media_one_c/Создание отгрузочной накладной.pdf'
    # await callback.message.edit_media()


@router.callback_query(F.data == 'command_0_2')
async def handle_0_2(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text=text_doc_to_study + one_c_buttons[2],
                                     reply_markup=build_button_menu())
    file_path = '../../media/media_one_c/Возврат от покупателя.pdf'
    # await callback.message.edit_media()


@router.callback_query(F.data == 'command_0_3')
async def handle_0_3(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text=text_doc_to_study + one_c_buttons[3],
                                     reply_markup=build_button_menu())
    file_path = '../../media/media_one_c/Создание контрагента.pdf'
    # await callback.message.edit_media()


@router.callback_query(F.data == 'command_0_4')
async def handle_0_3(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text=text_doc_to_study + one_c_buttons[4],
                                     reply_markup=build_button_menu())
    file_path = '../../media/media_one_c/Создание номенклатуры.pdf'
    # await callback.message.edit_media()
