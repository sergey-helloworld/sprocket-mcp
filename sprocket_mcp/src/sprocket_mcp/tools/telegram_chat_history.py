from redis import Redis
from datetime import date
from typing import Final, Any
import json

class TelegramChatHistory:
    CACHE_PREFIX: Final[str] = "telegram-chat-history"
    
    def __init__(self, redis_client: Redis) -> None:
        self.redis_client = redis_client

    def get_by_chat_id(
        self, 
        bot_id: str, 
        chat_id: int, 
        date: date, 
        offset_from: int = -10, 
        offset_to: int = -1
    ) -> list[dict[str, Any]]:
        history = self.redis_client.lrange(
            f"{self.CACHE_PREFIX}-{bot_id}-{chat_id}-{date}", 
            offset_from,
            offset_to
        )

        return [json.loads(h) for h in history]

    def store(self, bot_id: str, chat_id: int, message: dict[str, Any]) -> int:
        return self.redis_client.rpush(
            f"{self.CACHE_PREFIX}-{bot_id}-{chat_id}-{date.today()}", 
            json.dumps(message)
        )