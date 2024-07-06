#!/usr/bin/env python3
"""
Variable Annotation
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum Mixed List"""
    sum: float = 0
    for n in mxd_lst:
        sum += n

    return sum