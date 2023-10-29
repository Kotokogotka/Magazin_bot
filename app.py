from aiogram import types
from loader import dp

from keyboard.keyboard import start_keyboard
from lexicon.lexiconRu import text_command
from data.config import ADMINS


@dp.message_handlers(commands='start')
async def process_start_command(message: types.Message):
    await message.answer(text_command['start'], reply_markup=start_keyboard)


@dp.message_handlers(text=text_command['admin_message'])
async def admin_mode_process(messag: types.Message):
    admin_id = messag.chat.id
    if admin_id not in ADMINS:
