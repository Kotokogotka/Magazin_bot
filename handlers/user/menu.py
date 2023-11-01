from aiogram.types import Message
from loader import dp
from filters import IsUser, IsAdmin

from keyboard.keyboard import admin_menu_keyboard as ad
from keyboard.keyboard import user_menu_keyboard as us


@dp.message_handler(IsAdmin(), commands='menu')
async def process_admin_menu(message: Message):
    await message.answer('Mеню', reply_markup=ad)


@dp.message_handler(IsUser(), commands='menu')
async def process_admin_menu(message: Message):
    await message.answer('Mеню', reply_markup=us)
