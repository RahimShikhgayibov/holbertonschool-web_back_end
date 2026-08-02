#!/usr/bin/env python3
"""
izah
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    izah
    """
    def multiplier_func(n: float) -> float:
        """
        izah
        """
        return n * multiplier

    return multiplier_func
