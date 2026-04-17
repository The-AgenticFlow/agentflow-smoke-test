#!/usr/bin/env python3
"""Tests for calc.py."""
from calc import add


def test_add_positive():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negative():
    assert add(-1, 1) == 0


if __name__ == "__main__":
    test_add_positive()
    test_add_zero()
    test_add_negative()
    print("All tests passed!")
