"""
Unit tests for Task 1: Fibonacci Generator.
"""
import unittest
from src.fibonacci import fibonacci_generator, get_fibonacci_sequence


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_first_terms(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(get_fibonacci_sequence(10), expected)

    def test_fibonacci_edge_cases(self):
        self.assertEqual(get_fibonacci_sequence(0), [])
        self.assertEqual(get_fibonacci_sequence(1), [0])
        self.assertEqual(get_fibonacci_sequence(2), [0, 1])

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            get_fibonacci_sequence(-1)

    def test_infinite_generator_consumption(self):
        gen = fibonacci_generator()
        results = [next(gen) for _ in range(6)]
        self.assertEqual(results, [0, 1, 1, 2, 3, 5])


if __name__ == "__main__":
    unittest.main()
