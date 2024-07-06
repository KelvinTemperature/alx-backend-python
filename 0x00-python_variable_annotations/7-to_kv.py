#!/usr/bin/env python3
"""
Variable Annotation
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """"To KV:tuple"""
  
    return (k, v**2)