#!/usr/bin/env python3
import sys


def convert(s):
    '''Convert to an integer.'''
    x = -1
    try:
        return int(s)
    except (ValueError,TypeError) as e:
        print("Converstion error {}"\
            .format(str(e)),
            file=sys.stderr)
        raise



def sqrt(x):
    ''' Compute square roots '''
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main(y):
    z=convert(y)
    try:
        print (sqrt(z))
    except ValueError as e:
        print (e, file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1])
