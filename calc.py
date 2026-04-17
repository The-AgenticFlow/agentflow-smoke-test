#!/usr/bin/env python3
"""Minimal calculator CLI for AgentFlow smoke test."""
import sys


def add(a, b):
    return a + b


def main():
    if len(sys.argv) != 4:
        print("Usage: calc.py <add> <num1> <num2>")
        sys.exit(1)
    op = sys.argv[1]
    if op != "add":
        print(f"Unknown operation: {op}")
        sys.exit(1)
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    print(add(a, b))


if __name__ == "__main__":
    main()
