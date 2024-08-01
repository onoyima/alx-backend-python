#!/usr/bin/env python3
"""Module for safe_first_element function"""
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of lst or None if lst is empty"""
    if lst:
        return lst[0]
    else:
        return None
