#!/usr/bin/env python3
"""Minimal calculator CLI for AgentFlow smoke test."""
import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def parse_args():
    """Parse command line arguments, handling negative numbers correctly.

    Uses manual sys.argv parsing to properly handle negative numbers
    that would otherwise be interpreted as flags by argparse.
    """
    if len(sys.argv) != 4:
        print("Usage: calc.py <add|subtract|sub> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]
    if operation not in ("add", "subtract", "sub"):
        print(f"Unknown operation: {operation}")
        sys.exit(1)

    try:
        num1 = int(sys.argv[2])
        num2 = int(sys.argv[3])
    except ValueError as e:
        print(f"Invalid number: {e}")
        sys.exit(1)

    return operation, num1, num2


def main():
    operation, num1, num2 = parse_args()
    if operation == "add":
        print(add(num1, num2))
    elif operation in ("subtract", "sub"):
        print(subtract(num1, num2))


if __name__ == "__main__":
    main()
