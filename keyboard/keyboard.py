from aiogram.types import ReplyKeyboardMarkup
from lexicon.lexiconRu import text_command

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.row(text_command['user_message'], text_command['admin_message'])
