#!/usr/bin/env python3
"""
izah
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    izah
    """
    return [(i, len(i)) for i in lst]
