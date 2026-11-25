import pandas as pd
from typing import Any, Final
from ...helpers.path_helper import PathHelper
import random

class ExcelVocabularyRandomizer:
   def get_random_words(
      self, 
      filename: str, 
      count: int, 
      params: dict[str, Any],
   ) -> list[dict[str, str]]:
      if count < 1:
         return []

      has_header_row = params.get("has_header_row")
      sheet_name = params.get("sheet_name") if params.get("sheet_name") is not None else 0
      filename = PathHelper.normalize_path(filename)
      count_from = 2 if has_header_row else 1
      word_count = self.__get_word_count(filename, sheet_name)
      random_indexes = []
      words = []

      while len(random_indexes) < count:
         random_indexes.append(random.randint(count_from, word_count))

      for i in random_indexes:
         line = pd.read_excel(
            filename,
            sheet_name,
            skiprows=range(1, i-1) if has_header_row else i-1,
            nrows=1,
            keep_default_na=False,
            header=0 if has_header_row else None,
         )

         mapped = {k: v[0] for k, v in line.items()}

         words.append(mapped)      

      return words

   def __get_word_count(self, filename: str, sheet_name: str | int) -> int:
      limit = 500
      offset = 0
      count = 0

      while True:
         values = pd.read_excel(
            filename,
            sheet_name,
            skiprows=offset,
            nrows=limit,
            keep_default_na=False,
            usecols=[0],
            header=None,
         )

         if values.empty:
            break

         count += len(values[0])
         offset += 500

      return count