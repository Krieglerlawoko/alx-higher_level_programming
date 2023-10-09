#!/usr/bin/python3
"""an inherited list class"""


class MyList(list):
    """sorted printing for built-in list class"""

    def print_sorted(self):
        """Print ascending ordered list"""
        print(sorted(self))
