#!/usr/bin/env python3

''' Determine if we are Windows or LINUX
    and catch a key press '''

try:
    import msvcrt
    
    def getkey():
        """ Wait for a keypress and return a single character string."""
        return msvcrt.getch()

except ImportError:
    
    import sys
    import tty
    import termios

    def getkey():
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch 


def main():
    getkey()


if __name__ == '__main__':
    main()
