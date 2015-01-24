"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from pythagorean_triplet import triplets_in_range

tr = triplets_in_range(200, 425)
for i in tr:
    if sum(i) == 1000:
        print (i[0]*i[1]*i[2])
