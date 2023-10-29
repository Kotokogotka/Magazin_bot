from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardRemove

from keyboard.keyboard import start_keyboard
from lexicon.lexiconRu import text_command
from data.config import ADMINS


@dp.message_handlers(commands='start')
async def process_start_command(message: types.Message):
    await message.answer(text_command['start'], reply_markup=start_keyboard)


@dp.message_handlers(text=text_command['admin_message'])
async def admin_mode_process(message: types.Message):
    admin_id = message.chat.id
    if admin_id not in ADMINS:
        ADMINS.append(admin_id)
    await message.answer(text_command['on_admin'], reply_markup=ReplyKeyboardRemove())


@dp.message_handlers(text=text_command['user_message'])
async def admin_mode_process(message: types.Message):
    admin_id = message.chat.id
    if admin_id not in ADMINS:
        ADMINS.append(admin_id)
    await message.answer(text_command['on_user'], reply_markup=ReplyKeyboardRemove())
