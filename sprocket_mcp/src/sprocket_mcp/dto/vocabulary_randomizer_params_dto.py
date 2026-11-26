from dataclasses import dataclass, field
from typing import Optional

@dataclass
class VocabularyRandomizerParamsDto:
    excel_sheet_names: list[str | int] = field(default_factory=list)
    excel_has_header_row: bool = False