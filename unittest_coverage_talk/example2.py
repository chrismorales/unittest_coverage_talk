# -*- coding: utf-8 -*-

def get_number(odd_number=False):
    """
    Return 1 if odd_number flag is True or 2 if odd_number flag is False
    """
    number = 2
    if odd_number is True:
        number = 1

    return number
