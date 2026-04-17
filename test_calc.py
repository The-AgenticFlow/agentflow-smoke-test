#!/usr/bin/env python3
"""Tests for calc.py."""
from calc import add, subtract


def test_add_positive():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negative():
    assert add(-1, 1) == 0


def test_subtract_positive():
    assert subtract(5, 3) == 2


def test_subtract_zero():
    assert subtract(5, 0) == 5


def test_subtract_negative():
    assert subtract(3, 5) == -2


if __name__ == "__main__":
    test_add_positive()
    test_add_zero()
    test_add_negative()
    test_subtract_positive()
    test_subtract_zero()
    test_subtract_negative()
    print("All tests passed!")
