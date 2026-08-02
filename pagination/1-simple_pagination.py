#!/usr/bin/env python3
"""Simple pagination modulu.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Səhifə nömrəsi və ölçüsünə əsasən indeksləri qaytarır.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset.
        """
        # Tip və diapazon yoxlamaları (isinstance istifadə olundu)
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        # Məlumatları və indeksləri götürürük
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        # Əgər başlanğıc indeks datadan böyükdürsə, boş list qaytarırıq
        if start_index >= len(dataset):
            return []

        # Düzgün aralığı dilimləyib qaytarırıq
        return dataset[start_index:end_index]
