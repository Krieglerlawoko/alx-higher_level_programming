1-my_list.py
#!/usr/bin/python3
"""inherited list class MyList defined"""


class MyList(list):
    """sorted printing the built-in list class implemented"""

    def print_sorted(self):
        """list in sorted ascending order printed"""
        print(sorted(self))
