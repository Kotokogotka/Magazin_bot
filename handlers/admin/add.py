from Magazin_bot.loader import dp, db
from Magazin_bot.filters import IsAdmin
from Magazin_bot.lexicon.lexiconRu import text_command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

category_cd = CallbackData('category', 'id', 'action')


@dp.message_handler(IsAdmin(), text=text_command['setting'])
async def process_admin_setting(message: Message):
    markup = InlineKeyboardMarkup()
    for idx, title in db.fetchall('SELECT * FROM categories'):
        markup.add(InlineKeyboardButton(
            title, callback_data=category_cd.new(id=idx,
                                                 action='view')))
    markup.add(InlineKeyboardButton(
        '+ Добавить категорию', callback_data='add_category'
    ))
    await message.answer('Настройки категории', reply_markup=markup)