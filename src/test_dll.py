# -*- coding=utf-8 -*-
"""Test LinkedList for random inputs."""
import pytest

NODE_TEST_ITEMS = [
    object,
    235,
]

@pytest.mark.paramertrize('')
def test_dll_node(item):