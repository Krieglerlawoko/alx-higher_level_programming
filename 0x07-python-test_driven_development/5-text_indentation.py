#!/usr/bin/python3
"""function that indents text"""

def text_indentation(text):
    """prints indented text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == ' ':
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < len(text) and text[count] == ' ':
                count += 1
            continue
        count += 1
    
