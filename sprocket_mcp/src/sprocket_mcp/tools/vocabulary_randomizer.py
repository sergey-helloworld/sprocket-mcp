from sprocket_mcp.services.vocabulary_randomizer.vocabulary_randomizer_factory import (
    VocabularyRandomizerFactory,
)
from typing import Any

class VocabularyRandomizer:
    def get_random_words(
        self, 
        source: str, 
        resource_id: str, 
        count: int, 
        params: dict[str, Any] = {}
    ) -> list[dict[str, str]]:
        randomizer = VocabularyRandomizerFactory.create_by_source_name(source)
        return randomizer.get_random_words(resource_id, count, params)