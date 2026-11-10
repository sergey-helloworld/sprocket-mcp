import pandas as pd
from pathlib import Path
from typing import Final, Any
from urllib.parse import urlsplit

class ExcelIo:
    STORAGE_PATH: Final[str] = "storage"

    def get_sheet_names(self, path_or_url: str) -> list[str]:
        excel_file = pd.ExcelFile(self.__normalize_path(path_or_url))
        return excel_file.sheet_names

    def read_excel(
        self, 
        path_or_url: str, 
        sheet_name: str | None = None
    ) -> list[dict[str, Any]]:
        return pd.read_excel(
            self.__normalize_path(path_or_url), 
            sheet_name
        ).to_dict()

    def __normalize_path(self, path_or_url: str) -> str:
        url_parts = urlsplit(path_or_url)
        if url_parts.scheme in ['https', 'http'] and url_parts.netloc != '':
            return path_or_url
        
        return f"{self.STORAGE_PATH}/{path_or_url}"