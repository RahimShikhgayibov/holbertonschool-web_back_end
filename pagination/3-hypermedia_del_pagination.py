#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination modulu.
"""
import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Silinmələrə qarşı davamlı indeks əsaslı səhifələmə edir.
        """
        # 1. İlk öncə datanı lüğət formasında götürürük
        indexed_data = self.indexed_dataset()

        # 2. İndeksin mövcud diapazonda olub-olmadığını assert ilə yoxlayırıq
        if index is None:
            index = 0
        assert isinstance(index, int) and 0 <= index < len(indexed_data)
        assert isinstance(page_size, int) and page_size > 0

        data_page = []
        current_index = index

        # 3. Lazımi sayda (page_size) element toplayana qədər dövr edirik
        while len(data_page) < page_size and current_index < len(indexed_data):
            item = indexed_data.get(current_index)
            # Əgər element silinməyibsə, siyahıya əlavə edirik
            if item is not None:
                data_page.append(item)
            # İndeksi hər bir halda 1 vahid artırırıq
            current_index += 1

        # 4. Gözlənilən dictionary strukturunu return edirik
        return {
            "index": index,
            "data": data_page,
            "page_size": page_size,
            "next_index": current_index
        }
