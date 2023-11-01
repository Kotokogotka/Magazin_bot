from loader import dp, db
from filters import IsAdmin
from lexicon.lexiconRu import text_command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from states import CategoryState
from hashlib import md5
from aiogram.dispatcher import FSMContext


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


@dp.callback_query_handlers(IsAdmin(), text='add_category')
async def add_category_callback(query: CallbackQuery):
    await query.message.delete()
    await query.message.answer(text_command['name category'])
    await CategoryState.title.set()


@dp.message_handler(IsAdmin(), state=CategoryState.title)
async def process_set_category(message: Message, state: FSMContext):
    category = message.text
    idx = md5(category.encode('utf-8')).hexdigest()
    db.query('INSERT INTO categories VALUE (?, ?)')

    await state.finish()
    await process_admin_setting(message)