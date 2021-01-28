#!/usr/bin/python3

import unittest

def digits(x):

    digs=[]
    while x != 0:
        div, mod = divmod(x,10)
        digs.append(mod)
        x = div
    return digs


def is_palendrome(x):
    digs = digits(x)
    for f, r in zip(digs, reversed(digs)):
        if f != r:
            return False
    return True


class Tests(unittest.TestCase):

    def test_negative(self):
        self.assertFalse(is_palendrome(1234))

    def test_positive(self):
        self.assertTrue(is_palendrome(1234321))

    def test_single_digit(self):
        self.assertTrue(is_palendrome(1))


if __name__ == "__main__":
    unittest.main()
