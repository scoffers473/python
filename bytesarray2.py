#!/usr/bin/python3
import sys

def main(filename):
    fh = open(filename, 'rb')
    try:
        ba = bytearray(fh.read())
        for byte in ba:
            print (byte)
    finally:
        fh.close

    fh.close()

if __name__ == "__main__":
        main(sys.argv[1])
