#!/usr/bin/env python3
from sys import argv
import reverse_geocoder

# This script reads a list of coordinates from a file (line by line) and prints
# the corresponding city

def locate(coordinates):
    for c in coordinates:
        c = c.replace(' ', '')
        c = (c.split(',')[0], c.split(',')[1])
        result = reverse_geocoder.search(c)[0]
        print('%10s, %-10s -> %s %s' % (c[0], c[1], result['name'], result['admin1']))

def main():
    if len(argv) != 2:
        print('Usage ./%s <coordinates_file>')
        exit(1)
    coordinates = open(argv[1]).read().split('\n')[:-1]
    locate(coordinates)

if __name__ == '__main__':
    main()
