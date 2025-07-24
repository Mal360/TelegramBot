from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.inline_keyboards.one_c_kb import build_one_c_kb
from keyboards.inline_keyboards.start_kb import build_start_kb

router = Router(name=__name__)

text_doc_to_study = 'Вот документ для изучения '


def start_message(message):
    return message.answer(text='Здравствуйте, что бы вы хотели узнать?', reply_markup=build_start_kb())


def wait(message):
    return message.edit_text(text='Ожидайте... 😊')


@router.message(CommandStart())
async def handle_start(message: Message):
    await start_message(message)


@router.callback_query(F.data == 'back')
async def handle_back(callback: CallbackQuery):
    # if callback.message.reply_markup != build_one_c_kb():
    #     await callback.message.edit_text(text=callback.message.text, reply_markup=build_start_kb())
    # else:
    await callback.message.delete()
    await start_message(callback.message)


@router.callback_query(F.data == 'menu')
async def handle_back(callback: CallbackQuery):
    await callback.message.delete()
    await start_message(callback.message)
