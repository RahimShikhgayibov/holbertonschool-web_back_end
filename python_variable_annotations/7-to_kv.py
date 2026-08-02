#!/usr/bin/env python3
"""tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """number."""
    return (k, float(v * v))
