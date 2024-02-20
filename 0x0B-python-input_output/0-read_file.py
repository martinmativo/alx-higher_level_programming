#!/usr/bin/python3

"""Defines a function that reads text files."""

def read_file(filename=""):

    """Defines a function that reads a text file (UTF8) and prints it to stdout."""

    with open(filename, "r", encoding = "UTF-8") as f:
        print(f.read())
