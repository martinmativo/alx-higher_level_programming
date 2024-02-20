#!/usr/bin/python3

"""File appending at end of string."""

def append_write(filename="", text=""):
    """
    Args:
        filename (str): name of the file.
        text (str): string of text to be appended
    Returns:
        The number of characters added.
    """
    with open("filename", "a", encoding="UTF-8"):
        return f.append(text)
