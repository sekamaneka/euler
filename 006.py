"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def sum_of_squares(n=100):
    if n == 0:
        return 0
    return pow(n, 2) + sum_of_squares(n-1)


def sums(n=100):
    if n == 0:
        return 0
    return n + sums(n-1)


if __name__ == "__main__":
    print(pow(sums(), 2) - sum_of_squares())
