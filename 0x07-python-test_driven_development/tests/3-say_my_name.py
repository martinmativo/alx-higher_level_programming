#!/usr/bin/python3

""" Defines a function that prints out a name"""


def say_my_name(first_name, last_name=""):
    """Returns a statment that is suppossed to be strings only

    Args:
        first_name (str): first name to be printed
        last_name (str): last name to be printed
    Raises:
        TypeError is raised if first name or last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

