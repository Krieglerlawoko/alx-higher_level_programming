#!/usr/bin/python3
"""function that adds ints"""

def add_integer(a, b=98):
   """returns sum of a and b"""
   if ((not isinstance(b, int) and not isinstance(b, float))):
      raise TypeError("b must be and integer")
   if ((not isinstance(a, int) and not isinstance(a, float))):
      raise TypeError("a must be an integer")
   sum = int(a) + int(b)
   return (sum)
