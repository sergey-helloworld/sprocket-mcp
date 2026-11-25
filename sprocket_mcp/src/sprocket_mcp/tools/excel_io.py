import pandas as pd
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit
from pathlib import Path
import os

class ExcelIo:
    def get_sheet_names(self, path_or_url: str) -> list[str]:
        excel_file = pd.ExcelFile(self.__normalize_path(path_or_url))
        return excel_file.sheet_names

    def read_excel(
        self, 
        path_or_url: str, 
        sheet_name: str | None = None,
        has_header_row: bool = False,
        limit: int = 1000,
        offset: int = 0,
    ) -> dict[str, Any]:
        offset = range(1, offset + 1) if has_header_row else offset

        return pd.read_excel(
            self.__normalize_path(path_or_url), 
            sheet_name if sheet_name is not None else 0,
            skiprows=offset,
            nrows=limit,
            keep_default_na=False
        ).to_dict()

    def __normalize_path(self, path_or_url: str) -> str:
        url_parts = urlsplit(path_or_url)
        if url_parts.scheme in ["https", "http"] and url_parts.netloc != "":
            return path_or_url
        
        project_root = Path(__file__).resolve().parents[3]
        return project_root / os.getenv("STORAGE_PATH", "") / path_or_url