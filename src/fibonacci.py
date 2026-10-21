"""
Task 1: Fibonacci Series Generator

Implements:
1. An infinite / bounded generator using Python's `yield` statement.
2. A helper to return the first N Fibonacci numbers as a list.
"""
from typing import Generator, List


def fibonacci_generator(limit: int = None) -> Generator[int, None, None]:
    """
    Generates Fibonacci numbers indefinitely or up to a specified count.

    :param limit: Optional maximum number of terms to yield.
    :yields: Sequential Fibonacci integers.
    """
    a, b = 0, 1
    count = 0
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1


def get_fibonacci_sequence(n: int) -> List[int]:
    """
    Convenience function returning the first n Fibonacci numbers as a list.

    :param n: Number of elements (n >= 0).
    :return: List of Fibonacci numbers.
    """
    if n < 0:
        raise ValueError("Sequence length must be non-negative.")
    return list(fibonacci_generator(limit=n))
