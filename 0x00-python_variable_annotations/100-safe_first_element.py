#!/usr/bin/env python3
"""
Variable Annotation
"""
from typing import Any, Optional, Sequence, List


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None