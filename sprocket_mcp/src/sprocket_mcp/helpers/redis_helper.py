from redis import Redis
import os

class RedisHelper:
    client: Redis = None

    @classmethod
    def get_redis_client(cls) -> Redis:
        if cls.client is None:
            cls.client = Redis(
                host=os.getenv("REDIS_HOST"),
                port=int(os.getenv("REDIS_PORT")), 
                decode_responses=True
            )

        return cls.client

    @classmethod
    def close_connection(cls) -> None:
        cls.client.close()
        cls.client = None