#!/usr/bin/python3

""" 

My noodling with slices
Take an input string (S) and an integer (N) and return two arrays
The first 0-N characters long
The second N+1 to len (S) long

"""

import sys

def solution (S,N):

    # Gte string length
    longLen = len(S)

    # Convert string to tuple
    longTup = tuple(S)

    # edfine our two slices
    firstTup=slice(0,N)
    secondTup=slice(N,longLen)

    # Now return as lists two slices of the tuple
    return list(longTup[firstTup]), list(longTup[secondTup])


def main (S,N):
    a,b=solution (S,N)
    print (a)
    print (b)


if __name__ == "__main__":
    main (sys.argv[1], int(sys.argv[2]) )
