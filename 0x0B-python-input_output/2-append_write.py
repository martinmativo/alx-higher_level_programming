#!/usr/bin/python3

"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 file.

    Args:
        filename (str):The name of the file to append to.
        text (str): String of text to be appended.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
