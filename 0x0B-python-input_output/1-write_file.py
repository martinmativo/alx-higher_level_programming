#!/usr/bin/python3

"""Defines a text-writing function."""


def write_file(filename="", text=""):

    """
    A function that writes a string to a text file (UTF8) and returns the number of characters written.
    
    Args:
        filename (str) : name of file to be written on.
        text (str): string to write to the file.
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return(f.write(text)

