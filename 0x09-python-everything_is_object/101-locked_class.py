#!/usr/bin/python3

"""Define a locked class."""


class LockedClass:
    """
    prevent user from instantiating new LockedClass attributes
    for enything apart from attributed called 'first_name'.
    """

    __slots__ = ['first_name']
