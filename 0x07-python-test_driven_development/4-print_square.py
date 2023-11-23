#!/usr/bin/bash
"""function prints a square"""


def print_square(size):
   """print a # square"""
   if size < 0:
      raise ValueError("size must be >= 0")
   if not isinstance(size, int):
      raise TypeError("size must be an integer")

   for a in range(size):
      [print("#", end="") for b in range(size)]
      print("")
