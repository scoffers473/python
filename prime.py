#!/usr/bin/python

from math import sqrt
from pprint import pprint as pp

def is_prime(x):
    if x < 2:
        return False
    for i in range (2, int(sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

primes = [ x for x in range(101) if is_prime(x)]

divisors = { x*x:(1, x, x*x) for x in range (101) if is_prime(x)}
pp(primes)
pp(divisors)
