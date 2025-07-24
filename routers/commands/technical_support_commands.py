from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.technical_support_kb import build_technical_support_kb

router = Router(name=__name__)


@router.callback_query(F.data == 'command_6')
async def handle_technical_support(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите подкатегорию', reply_markup=build_technical_support_kb())
