#!/usr/bin/env python3
"""
Variable Annotation
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
  """Sum List"""
  sum: float = 0
  for n in input_list:
      sum += n
      
  return sum