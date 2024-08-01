#!/usr/bin/env python3
"""Module for safely_get_value function"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the value of dct[key] or default if key is not in dct"""
    if key in dct:
        return dct[key]
    else:
        return default
