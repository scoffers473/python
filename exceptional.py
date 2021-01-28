#!/usr/bin/env python3
import sys
import math
''' A module for demonstrating exceptions. '''

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

def string_log(s):
    v = convert(s)
    return math.log(v)
