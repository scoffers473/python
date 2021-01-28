#!/usr/bin/python

from math import factorial

f = [len(str(factorial(x))) for x in range(20)]

print(f)
