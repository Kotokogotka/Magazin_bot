from aiogram.types import Message
from Magazin_bot.loader import dp
from Magazin_bot.filters import IsUser, IsAdmin

from Magazin_bot.keyboard.keyboard import admin_menu_keyboard, user_menu_keyboard


@dp.message_handlers(IsAdmin(), commands='menu')
async def process_admin_menu(message: Message):
    await message.answer('Mеню', reply_markup=admin_menu_keyboard)


@dp.message_handlers(IsUser(), commands='menu')
async def process_admin_menu(message: Message):
    await message.answer('Mеню', reply_markup=user_menu_keyboard)
