#!/usr/bin/python3
"""funciton indents text"""


def text_indentation(text):
    """prints indented text"""
    if not isinstance(text, str):
       raise TypeError("text must be a string")

    x = 0
    while text[x] == ' ' and x < len(text):
       x += 1
       while text[c] == ' ' and x < len(text):
          x += 1
       continue
    x += 1
