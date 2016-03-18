# -*- encoding: utf-8 -*-
"""A module for seeing if you have the right amount of parantheses."""


def proper_parens(string):
    """Test if the number of "(" matches the number of ")"."""
    status = 0
    for char in string.strip():
        if char == "(":
            status += 1
        elif char == ")":
            status -= 1
    if status:
        return status / abs(status)
    else:
        return status
