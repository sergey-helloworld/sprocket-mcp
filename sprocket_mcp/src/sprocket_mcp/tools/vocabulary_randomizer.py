from ..services.vocabulary_randomizer.vocabulary_randomizer_factory import (
    VocabularyRandomizerFactory,
)
from ..dto.vocabulary_randomizer_params_dto import VocabularyRandomizerParamsDto
from typing import Any

class VocabularyRandomizer:
    def get_random_words(
        self, 
        source: str, 
        resource_id: str, 
        count: int, 
        params: VocabularyRandomizerParamsDto | None = VocabularyRandomizerParamsDto(),
    ) -> list[dict[str, str]]:
        randomizer = VocabularyRandomizerFactory.create_by_source_name(source)
        return randomizer.get_random_words(resource_id, count, params)