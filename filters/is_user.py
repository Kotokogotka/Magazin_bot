from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from Magazin_bot.data.config import ADMINS


class IsUser(BoundFilter):
    async def check(self, message: Message) -> bool:
        return message.from_user.id not in ADMINS