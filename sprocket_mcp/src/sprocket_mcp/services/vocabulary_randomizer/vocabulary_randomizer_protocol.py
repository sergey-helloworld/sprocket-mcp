from typing import Protocol, Any

class VocabularyRandomizerProtocol(Protocol):
    def get_random_words(
        self, 
        resource_id: str, 
        count: int, 
        params: dict[str, Any]
    ) -> list[dict[str, str]]:
        pass