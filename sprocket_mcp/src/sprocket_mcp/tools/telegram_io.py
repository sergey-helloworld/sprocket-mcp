import telegram
import os
from typing import Final, Any

class TelegramIo:
    TOKEN_PREFIX: Final[str] = "TELEGRAM_BOT_TOKEN_"

    async def send_message(self, bot_id: str, chat_id: int, message: str) -> dict[str, Any]:
        bot = telegram.Bot(os.getenv(self.TOKEN_PREFIX + bot_id))
        async with bot:
            return (await bot.send_message(chat_id, message)).to_dict()

    async def get_updates(
        self, 
        bot_id: str, 
        offset: int|None = None,
        timeout: int|None = None,
        chat_id: int|None = None
    ) -> list[dict[str, Any]]:
        bot = telegram.Bot(os.getenv(self.TOKEN_PREFIX + bot_id))

        async with bot:
            updates = await bot.get_updates(offset=offset, timeout=timeout)

            if chat_id is None:
                updates = tuple(u for u in updates if u.message.chat_id == chat_id)

            return [u.to_dict() for u in updates]