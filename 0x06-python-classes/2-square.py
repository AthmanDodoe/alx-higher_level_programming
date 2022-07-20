#!/usr/bin/python3
""" Module square """


class Square:
    """ Class that defines a square"""


def __init__(self, size=0):
    """ Initialize square
    Args:
        size (int): Size of the square
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >=0')
    else:
        self.size = size
