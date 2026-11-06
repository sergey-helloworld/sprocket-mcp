from urllib.parse import urlsplit
from sprocket_mcp.tools.excel_io import ExcelIo
import os
import time

def is_url(string: str) -> str:
    url_parts = urlsplit(string)
    if url_parts.scheme in ['https', 'http'] and url_parts.netloc != '':
        return True

    return False

# excel_io = ExcelIo()
# print(excel_io.get_sheet_names("vocabulary.xlsx"))
print(os.environ.get('PYTHONUNBUFFERED'), end="")
time.sleep(5)
print(' the end')