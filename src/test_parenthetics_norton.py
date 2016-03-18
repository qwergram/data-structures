# -*- coding: utf-8 -*-
"""Test proper_parenthetics_norton for validity"""
import pytest


PAREN_TABLE = {
    (")", -1),
    ("(", 1),
    ("()", 0),
    ("", 0),
    ("hhhhhhh", 0),
    ("hhhhhhh)", -1),
    ("hhhhhhh))))", -1),
    ("(hh(hh(hh(h))))", 0),
    ("(hh(h(h(hh(h))))", 1),
    ("]]]]]]", 0),
}


@pytest.mark.parametrize('test_string, expected', PAREN_TABLE)
def test_paren(test_string, expected):
    """Assert parenthetical return correct int."""
    from proper_parenthetics_norton import proper_parens
    assert proper_parens(test_string) == expected
