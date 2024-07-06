#!/usr/bin/env python3
"""
Variable Annotation
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst):
    return [(i, len(i)) for i in lst]