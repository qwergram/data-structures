# -*- coding: utf-8 -*-
"""Parenthetical whitboard challenge."""


def paren(string_):
    """Return a number based on parenthesis status."""
    tally = 0
    for i, k in enumerate(string_):
        if k == ')':
            tally += -1
        if k == '(':
            tally += 1
        if tally < 0:
            return -1
    if tally > 0:
        return 1
    return tally
