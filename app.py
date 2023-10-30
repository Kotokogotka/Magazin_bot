from aiogram import types, executor
from loader import dp, bot, db
from aiogram.types import ReplyKeyboardRemove
from logging import basicConfig, INFO

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


async def on_startup(dp):
    basicConfig(level=INFO)
    db.create_table()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)