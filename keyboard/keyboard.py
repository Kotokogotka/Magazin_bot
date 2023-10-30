from aiogram.types import ReplyKeyboardMarkup
from lexicon.lexiconRu import text_command

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.row(text_command['user_message'], text_command['admin_message'])

admin_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
admin_menu_keyboard.add(text_command['setting'])
admin_menu_keyboard.add(text_command['questions'], text_command['orders'])

user_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
admin_menu_keyboard.add(text_command['catalog'])
admin_menu_keyboard.add(text_command['cart'])
admin_menu_keyboard.add(text_command['delivery status'])