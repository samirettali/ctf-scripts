#!/usr/bin/env python3

# Translates a string into another one for an entire file

from sys import argv

table = dict()

def load_table(filename):
    with open(filename, 'r') as f:
        for line in f:
            symbol, translation = line.replace('\n', '').split('\t')
            table[symbol] = translation

def translate(string, separator = ''):
    translated_string = ''
    for char in string:
        translated_string += table[char] + separator
    print(translated_string)

def main():
    if len(argv) < 3:
        print('Usage %s <dictionary> <string>')
        exit(1)
    dictionary = argv[1]
    string = argv[2]

    load_table(dictionary)

    if len(argv) == 4:
        translate(string, argv[3])
    else:
        translate(string)

if __name__ == '__main__':
    main()
