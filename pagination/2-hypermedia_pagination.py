#!/usr/bin/env python3
"""Hypermedia pagination modulu.
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
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Səhifələmə haqqında bütün hypermedia məlumatlarını qaytarır.
        """
        # 1. Arqumentlərin düzgünlüyünü assert ilə yoxlayırıq
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        # 2. get_page metodunu yenidən istifadə edirik
        data = self.get_page(page, page_size)

        # 3. Ümumi səhifə sayını hesablamaq üçün math.ceil istifadə edirik
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # 4. Növbəti səhifə nömrəsini təyin edirik
        next_page = page + 1 if page < total_pages else None

        # 5. Əvvəlki səhifə nömrəsini təyin edirik
        prev_page = page - 1 if page > 1 else None

        # 6. Tələb olunan struktura uyğun dictionary qaytarırıq
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
