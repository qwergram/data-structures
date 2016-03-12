# -*- encoding: utf-8 -*-

def proper_parens(string):
    status = 0
    for char in string:
        if char == "(":
            status += 1
        elif char == ")":
            status -= 1
    if status:
        return status / abs(status)
    else:
        return status

assert proper_parens("()") == 0
assert proper_parens("(") == 1
assert proper_parens(")") == -1
assert proper_parens("))") == -1
assert proper_parens("((") == 1
assert proper_parens("((()") == 1
assert proper_parens("())))") == -1
assert proper_parens("((((()))))") == 0
