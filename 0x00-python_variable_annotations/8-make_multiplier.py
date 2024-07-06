#!/usr/bin/env python3
"""
Variable Annotation
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
  """Make Multipler"""
  return lambda x: x * multiplier