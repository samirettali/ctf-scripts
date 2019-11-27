#!/usr/bin/env python3
import string
from sys import argv


# This script converts a string in the phone keypad presses necessary to write
# that string

def get_key(char):
    keys = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0,
            'a': 22,
            'b': 222,
            'c': 2222,
            'd': 33,
            'e': 333,
            'f': 3333,
            'g': 44,
            'h': 444,
            'i': 4444,
            'j': 55,
            'k': 555,
            'l': 5555,
            'm': 66,
            'n': 666,
            'o': 6666,
            'p': 77,
            'q': 777,
            'r': 7777,
            's': 77777,
            't': 88,
            'u': 888,
            'v': 8888,
            'w': 99,
            'x': 999,
            'y': 9999,
            'z': 99999,
            }
    return keys[char]


def calculate(string):
    s = 0
    for char in string:
        number = get_key(char)
        for c in str(number):
            s += int(c)
    return s


def main():
    if len(argv) != 2:
        print('Usage: ./%s <string>' % argv[0])
        exit(1)

    print(calculate(argv[1].lower()))


if __name__ == '__main__':
    main()
