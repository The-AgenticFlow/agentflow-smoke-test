#!/usr/bin/env python3
"""Minimal calculator CLI for AgentFlow smoke test."""
import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    if len(sys.argv) != 4:
        print("Usage: calc.py <add|sub> <num1> <num2>")
        sys.exit(1)
    op = sys.argv[1]
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    if op == "add":
        print(add(a, b))
    elif op == "sub":
        print(subtract(a, b))
    else:
        print(f"Unknown operation: {op}")
        sys.exit(1)


if __name__ == "__main__":
    main()
