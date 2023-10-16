#!/usr/bin/python3
"""locked class."""


class LockedClass:
    """Prevent user from instantiating new LockedClass attributes
    for anything except for 'first_name'.
    """

    __slots__ = ["first_name"]
