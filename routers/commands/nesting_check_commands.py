from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.base_buttons import build_button_menu
from keyboards.inline_keyboards.nesting_check_kb import (build_nesting_check_kb,
                                                         build_nesting_check_1_kb,
                                                         build_nesting_check_2_kb)
from routers.commands.base_commands import wait

router = Router(name=__name__)


@router.callback_query(F.data == 'command_5')
async def handle_nesting_check(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите подкатегорию', reply_markup=build_nesting_check_kb())


@router.callback_query(F.data == 'command_5_0')
async def handle_nesting_check(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите подподкатегорию', reply_markup=build_nesting_check_1_kb())


@router.callback_query(F.data == 'command_5_0_0')
async def handle_nesting_check(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите подподкатегорию', reply_markup=build_nesting_check_2_kb())


@router.callback_query(F.data == 'command_5_0_0_0')
async def handle_nesting_check(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text='Просто проверка, ничего важного', reply_markup=build_button_menu())


@router.callback_query(F.data == 'command_5_0_1')
async def handle_nesting_check(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text='Просто проверка, ничего важного', reply_markup=build_button_menu())


@router.callback_query(F.data == 'command_5_1')
async def handle_nesting_check(callback: CallbackQuery):
    await wait(callback.message)
    await callback.message.edit_text(text='Просто проверка, ничего важного', reply_markup=build_button_menu())


@router.callback_query(F.data == 'command_5_2')
async def handle_nesting_check(callback: CallbackQuery):
    await wait(callback.message)
