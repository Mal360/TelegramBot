from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.about_company_kb import build_about_company_kb


router = Router(name=__name__)


@router.callback_query(F.data == 'command_4')
async def handle_about_company(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите подкатегорию', reply_markup=build_about_company_kb())
