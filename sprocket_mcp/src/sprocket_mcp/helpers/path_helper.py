import os
from pathlib import Path
from urllib.parse import urlsplit

class PathHelper:
    @staticmethod
    def normalize_path(path_or_url: str) -> str:
        url_parts = urlsplit(path_or_url)
        if url_parts.scheme in ["https", "http"] and url_parts.netloc != "":
            return path_or_url
        
        project_root = Path(__file__).resolve().parents[3]

        return project_root / os.getenv("STORAGE_PATH", "") / path_or_url