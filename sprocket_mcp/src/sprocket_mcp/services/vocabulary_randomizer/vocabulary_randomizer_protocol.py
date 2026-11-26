from typing import Protocol, Any
from ...dto.vocabulary_randomizer_params_dto import VocabularyRandomizerParamsDto

class VocabularyRandomizerProtocol(Protocol):
    def get_random_words(
        self, 
        resource_id: str, 
        count: int, 
        params: VocabularyRandomizerParamsDto,
    ) -> list[dict[str, str]]:
        pass