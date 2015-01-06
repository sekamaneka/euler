"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

def find(n):
    for i in range(20,0,-1):
        if n%i!=0:
            return
    return 'done'

for i in range (2500000,509005000,20):
    if (find(i)):
        print(i)
        break
        
