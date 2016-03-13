# -*- coding: utf-8 -*-
"""Parenthetical whitboard challenge."""


def parenthetical(string_):
    """Return a number based on string."""
    if len(string_) % 2 != 0:
        return 1
    str_size = len(string_)
    str = string_
    while str_size != 0:
        str = str.replace('()', '')
        if str_size == len(str):
            return -1
        str_size = len(str)
    return 0
