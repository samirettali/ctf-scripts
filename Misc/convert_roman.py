#!/usr/bin/env python3
from sys import argv

# This script converts a list of Roman numbers to decimal

def value(r): 
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000
    return -1
  
def romanToDecimal(str): 
    res = 0
    i = 0
    while (i < len(str)): 
        s1 = value(str[i]) 
        if (i+1 < len(str)): 
            s2 = value(str[i+1]) 
            if (s1 >= s2): 
                res = res + s1 
                i = i + 1
            else: 
                res = res + s2 - s1 
                i = i + 2
        else: 
            res = res + s1 
            i = i + 1
    return res 
  
def main():
    if len(argv) < 2:
        print('Usage: ./%s <numbers>' % argv[0])
        exit(1)

    for roman in argv[1:]:
        print(romanToDecimal(roman), end=' ')  
    print()

if __name__ == '__main__':
    main()
