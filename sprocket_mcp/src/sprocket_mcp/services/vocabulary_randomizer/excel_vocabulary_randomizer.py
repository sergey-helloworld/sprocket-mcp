import pandas as pd
from typing import Any, Final
from ...helpers.path_helper import PathHelper
from ...dto.vocabulary_randomizer_params_dto import VocabularyRandomizerParamsDto
import random
from functools import reduce

class ExcelVocabularyRandomizer:
   def get_random_words(
      self, 
      filename: str, 
      count: int, 
      params: VocabularyRandomizerParamsDto | None = VocabularyRandomizerParamsDto()  
   ) -> list[dict[str, str]]:
      if count < 1:
         return []

      has_header_row = params.excel_has_header_row
      sheet_names = params.excel_sheet_names if params.excel_sheet_names else [0]
      filename = PathHelper.normalize_path(filename)
      count_from = 2 if has_header_row else 1
      word_positions = self.__get_word_positions(filename, sheet_names, has_header_row)
      random_indexes = []
      words = []

      while len(random_indexes) < count:
         random_indexes.append(random.randint(count_from, len(word_positions)) - 1)

      for i in random_indexes:
         position = word_positions[i]["position"]
         sheet_name = word_positions[i]["sheet_name"]

         line = pd.read_excel(
            filename,
            sheet_name,
            skiprows=range(1, position) if has_header_row else position,
            nrows=1,
            keep_default_na=False,
            header=0 if has_header_row else None,
         )

         mapped = {k: v[0] for k, v in line.items()}

         words.append(mapped)      

      return words
   
   def __get_word_positions(
      self, 
      filename: str, 
      sheet_names: list[str | int],
      has_header_row: bool = False,
   ) -> list[dict[str, str | int]]:
      word_positions = []
      for sheet_name in sheet_names:
         word_count = self.__get_word_count(filename, sheet_name)
         for i in range(1 if has_header_row else 0, word_count):
            word_positions.append({"position": i, "sheet_name": sheet_name})
      
      return word_positions

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