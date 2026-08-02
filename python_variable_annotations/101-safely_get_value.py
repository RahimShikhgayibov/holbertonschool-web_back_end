#!/usr/bin/env python3
"""
izah
"""
from typing import Mapping, Any, Union, TypeVar, Optional

# T adında bir TypeVar yaradırıq
T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Optional[T] = None
) -> Union[Any, T]:
    """
    izah
    """
    if key in dct:
        return dct[key]
    else:
        return default
