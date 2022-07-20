#!/usr/bin/python3
from curses.ascii import isdigit


def safe_print_integer(value):
    try:
        isinstance(value, int)
        print("{:d}".format(value))
        return True
    except Exception:
        return False