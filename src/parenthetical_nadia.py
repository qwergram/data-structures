# -*- coding: utf-8 -*-
"""Parenthetical whitboard challenge."""


def parenthetical(string_):
    """Return a number based on string."""
    newstr = u""
    for i in string_:
        if i == '(' or i == ')':
            newstr += i
    if len(newstr) % 2 != 0:
        return 1
    str_size = len(newstr)
    str_ = newstr
    while str_size != 0:
        str_ = str_.replace('()', '')
        if str_size == len(str_):
            return -1
        str_size = len(str_)
    return 0
