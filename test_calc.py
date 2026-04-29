#!/usr/bin/env python3
"""Tests for calc.py."""
import subprocess
import sys
from unittest.mock import patch
from calc import add, subtract, parse_args


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


def test_cli_sub_positive():
    """Test CLI 'sub' alias with positive numbers."""
    output, code = run_cli(["sub", "5", "3"])
    assert code == 0
    assert output == "2"


def test_cli_sub_zero():
    """Test CLI 'sub' alias resulting in zero."""
    output, code = run_cli(["sub", "5", "5"])
    assert code == 0
    assert output == "0"


def test_cli_sub_negative_result():
    """Test CLI 'sub' alias with negative result."""
    output, code = run_cli(["sub", "3", "5"])
    assert code == 0
    assert output == "-2"


def test_cli_sub_from_negative():
    """Test CLI 'sub' alias from negative number."""
    output, code = run_cli(["sub", "-5", "3"])
    assert code == 0
    assert output == "-8"


def test_cli_sub_with_negatives():
    """Test CLI 'sub' alias subtracting negative number."""
    output, code = run_cli(["sub", "-1", "-2"])
    assert code == 0
    assert output == "1"


# parse_args() Unit Tests
def test_parse_args_basic_add():
    """Test parse_args with basic add operation."""
    with patch.object(sys, 'argv', ['calc.py', 'add', '2', '3']):
        operation, num1, num2 = parse_args()
        assert operation == 'add'
        assert num1 == 2
        assert num2 == 3


def test_parse_args_basic_subtract():
    """Test parse_args with basic subtract operation."""
    with patch.object(sys, 'argv', ['calc.py', 'subtract', '5', '3']):
        operation, num1, num2 = parse_args()
        assert operation == 'subtract'
        assert num1 == 5
        assert num2 == 3


def test_parse_args_single_negative():
    """Test parse_args with one negative number: calc.py add -1 2."""
    with patch.object(sys, 'argv', ['calc.py', 'add', '-1', '2']):
        operation, num1, num2 = parse_args()
        assert operation == 'add'
        assert num1 == -1
        assert num2 == 2


def test_parse_args_two_negatives():
    """Test parse_args with two negative numbers: calc.py add -5 -3."""
    with patch.object(sys, 'argv', ['calc.py', 'add', '-5', '-3']):
        operation, num1, num2 = parse_args()
        assert operation == 'add'
        assert num1 == -5
        assert num2 == -3


def test_parse_args_large_negatives():
    """Test parse_args with large negative numbers."""
    with patch.object(sys, 'argv', ['calc.py', 'add', '-1000000', '-999999']):
        operation, num1, num2 = parse_args()
        assert operation == 'add'
        assert num1 == -1000000
        assert num2 == -999999


def test_parse_args_negative_with_subtract():
    """Test parse_args with negative numbers in subtract operation."""
    with patch.object(sys, 'argv', ['calc.py', 'subtract', '-10', '-5']):
        operation, num1, num2 = parse_args()
        assert operation == 'subtract'
        assert num1 == -10
        assert num2 == -5


def test_parse_args_basic_sub():
    """Test parse_args with 'sub' alias."""
    with patch.object(sys, 'argv', ['calc.py', 'sub', '5', '3']):
        operation, num1, num2 = parse_args()
        assert operation == 'sub'
        assert num1 == 5
        assert num2 == 3


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
    test_cli_sub_positive()
    test_cli_sub_zero()
    test_cli_sub_negative_result()
    test_cli_sub_from_negative()
    test_cli_sub_with_negatives()
    test_parse_args_basic_add()
    test_parse_args_basic_subtract()
    test_parse_args_single_negative()
    test_parse_args_two_negatives()
    test_parse_args_large_negatives()
    test_parse_args_negative_with_subtract()
    test_parse_args_basic_sub()
    print("All tests passed!")
