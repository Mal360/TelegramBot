from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaDocument

from keyboards.inline_keyboards.base_buttons import build_button_menu
from keyboards.inline_keyboards.equipment_maintenance_kb import build_equipment_maintenance_kb

router = Router(name=__name__)


@router.callback_query(F.data == 'command_3')
async def handle_equipment_maintenance(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите подкатегорию', reply_markup=build_equipment_maintenance_kb())
