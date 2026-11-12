from redis import Redis

class RedisHelper:
    client: Redis = None

    @classmethod
    def get_redis_client(cls) -> Redis:
        if cls.client is None:
            cls.client = Redis(host='host.docker.internal', port=6379, decode_responses=True)

        return cls.client

    @classmethod
    def close_connection(cls) -> None:
        cls.client.close()
        cls.client = None