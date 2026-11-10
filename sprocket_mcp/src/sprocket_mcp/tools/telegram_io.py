import telegram
import os
from typing import Final

class TelegramIo:
    TOKEN_PREFIX: Final[str] = "TELEGRAM_BOT_TOKEN_"

    async def send_message(self, bot_id: str, chat_id: int, message: str) -> telegram.Message:
        bot = telegram.Bot(os.getenv(self.TOKEN_PREFIX + bot_id))
        async with bot:
            return await bot.send_message(chat_id, message)

    async def get_updates(
        self, 
        bot_id: str, 
        offset: int,
        chat_id: int|None = None
    ) -> tuple[telegram.Update]:
        bot = telegram.Bot(os.getenv(self.TOKEN_PREFIX + bot_id))

        async with bot:
            updates = await bot.get_updates(offset=offset)

            if chat_id is None:
                return updates

            return tuple(u for u in updates if u.message.chat_id == chat_id)