#!/usr/bin/env python3
"""
IZAH
"""
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    izah
    """
    if lst:
        return lst
    else:
        return None
