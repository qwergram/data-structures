# -*- coding: utf-8 -*-
"""Test for parenthetical_nadia.py."""
import pytest


PAREN_TABLE = {
    ("", 0),
    ("()", 0),
    ("())", -1),
    (")()())", -1),
    (")()", -1),
    ("(hi)", 0),
    ("(((((((", 1),
    ("(()", 1),
    ("(hi", 1),
    (")hi", -1),
    ("hello(())", 0),
}


@pytest.mark.parametrize('string_, result', PAREN_TABLE)
def test_parenthetical(string_, result):
    """Assert parenthetical return correct int."""
    from parenthetical_nadia import paren
    assert paren(string_) == result
