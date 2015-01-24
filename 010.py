"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import math


def nth_prime(number):
        primes = [2]
        i = 1
        index = 1
        while primes[-1] < number:
                i += 2
                prime = True
                i_root = math.sqrt(i)
                for j in (primes):
                        if i % j == 0:
                            prime = False
                            break
                        if j > i_root:
                                break
                if prime:
                        primes.append(i)
                        index += 1
        return sum(primes[:-1:])

print(nth_prime(2000000))
