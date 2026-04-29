#!/usr/bin/env python3
"""Tests for calc.py."""
import subprocess
import sys
from calc import add, subtract


def test_add_positive():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negative():
    assert add(-1, 1) == 0


def test_add_two_negatives():
    """Test adding two negative numbers."""
    assert add(-5, -3) == -8


def test_add_negative_positive():
    """Test adding negative and positive number."""
    assert add(-1, 2) == 1
    assert add(5, -3) == 2


def test_add_large_negatives():
    """Test with large negative numbers."""
    assert add(-1000, -2000) == -3000
    assert add(-999999, 1) == -999998


# Subtraction Tests
def test_subtract_positive():
    assert subtract(5, 3) == 2


def test_subtract_zero():
    assert subtract(5, 5) == 0


def test_subtract_negative():
    assert subtract(-1, -2) == 1


def test_subtract_from_negative():
    assert subtract(-5, 3) == -8


# CLI Integration Tests
def run_cli(args):
    """Helper to run calc.py as a subprocess."""
    result = subprocess.run(
        [sys.executable, "calc.py"] + args,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip(), result.returncode


def test_cli_add_positive():
    """Test CLI with positive numbers."""
    output, code = run_cli(["add", "5", "3"])
    assert code == 0
    assert output == "8"


def test_cli_add_single_negative():
    """Test CLI with one negative number: calc.py add -1 2"""
    output, code = run_cli(["add", "-1", "2"])
    assert code == 0
    assert output == "1"


def test_cli_add_two_negatives():
    """Test CLI with two negative numbers: calc.py add -5 -3"""
    output, code = run_cli(["add", "-5", "-3"])
    assert code == 0
    assert output == "-8"


def test_cli_add_negative_result():
    """Test CLI that produces negative result."""
    output, code = run_cli(["add", "-10", "-20"])
    assert code == 0
    assert output == "-30"


def test_cli_invalid_operation():
    """Test CLI with invalid operation."""
    output, code = run_cli(["multiply", "5", "3"])
    assert code != 0


def test_cli_missing_args():
    """Test CLI with missing arguments."""
    output, code = run_cli(["add"])
    assert code != 0


def test_cli_subtract_positive():
    """Test CLI subtraction with positive numbers."""
    output, code = run_cli(["subtract", "5", "3"])
    assert code == 0
    assert output == "2"


def test_cli_subtract_zero():
    """Test CLI subtraction resulting in zero."""
    output, code = run_cli(["subtract", "5", "5"])
    assert code == 0
    assert output == "0"


def test_cli_subtract_negative_result():
    """Test CLI subtraction with negative result."""
    output, code = run_cli(["subtract", "3", "5"])
    assert code == 0
    assert output == "-2"


def test_cli_subtract_from_negative():
    """Test CLI subtraction from negative number."""
    output, code = run_cli(["subtract", "-5", "3"])
    assert code == 0
    assert output == "-8"


def test_cli_subtract_with_negatives():
    """Test CLI subtracting negative number."""
    output, code = run_cli(["subtract", "-1", "-2"])
    assert code == 0
    assert output == "1"


if __name__ == "__main__":
    test_add_positive()
    test_add_zero()
    test_add_negative()
    test_add_two_negatives()
    test_add_negative_positive()
    test_add_large_negatives()
    test_subtract_positive()
    test_subtract_zero()
    test_subtract_negative()
    test_subtract_from_negative()
    test_cli_add_positive()
    test_cli_add_single_negative()
    test_cli_add_two_negatives()
    test_cli_add_negative_result()
    test_cli_invalid_operation()
    test_cli_missing_args()
    test_cli_subtract_positive()
    test_cli_subtract_zero()
    test_cli_subtract_negative_result()
    test_cli_subtract_from_negative()
    test_cli_subtract_with_negatives()
    print("All tests passed!")
