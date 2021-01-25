#!/usr/bin/python3
"""
This takes an input word and prints out a count of uneven letters
for example   in aabbc we have one uneven letter (c). In hello we have 3 (hme and o)
"""

import sys
from collections import Counter

def solution  (S):
    removal=0
    counter = Counter(S)
    for letters in S:
        if  counter[letters]%2 != 0:
            removal += 1
    return removal


def main (S):
    ans = solution(S)
    print(" For the word ",S, " we would have to remove ", ans," letters to make it even")


if __name__ == "__main__":
    main(sys.argv[1])
