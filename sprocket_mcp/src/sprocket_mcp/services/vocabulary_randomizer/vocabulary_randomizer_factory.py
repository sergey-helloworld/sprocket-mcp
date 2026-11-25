from .vocabulary_randomizer_protocol import VocabularyRandomizerProtocol
from .excel_vocabulary_randomizer import ExcelVocabularyRandomizer

class VocabularyRandomizerFactory:
    @staticmethod
    def create_by_source_name(source_name: str) -> VocabularyRandomizerProtocol:
        if source_name == "excel":
            return ExcelVocabularyRandomizer()

        raise Exception("Given source not found")