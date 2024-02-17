#!usr/bin/python3

"""Prints a square."""


def print_square(size):
    """Defines a function to print a square with #character.
    Args:
        size (int): The size in length of the square

    Raises:
        ValueError: If size is less than 0
        TypeError: If size is a float and is less than 0
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
