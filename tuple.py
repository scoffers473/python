#!/usr/bin/env python3

import sys
import argparse

def minmax(items):
    return min(items), max(items)


def main(tupe):
    type(tupe)
    lower, upper = minmax(tupe)
    print ("Lower is ", lower)
    print ("Upper is ", upper)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', nargs='+', type=int)
    args = parser.parse_args()
    main(args.data)
