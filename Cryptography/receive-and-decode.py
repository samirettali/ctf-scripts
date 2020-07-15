#!/usr/bin/env python3
from math import gcd
import string
import json
import base64
import codecs
import Crypto.Util.number
from pwn import remote

# This script receives an encoded/encrypted string and tries to decode it
# against various ciphers (must be improved and cleaned up).

def rot(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
       char = text[i]
       # Encrypt uppercase characters in plain text
       
       if (char.isupper()):
          result += chr((ord(char) + s-65) % 26 + 65)
       # Encrypt lowercase characters in plain text
       elif char.islower():
          result += chr((ord(char) + s - 97) % 26 + 97)
       else:
           result += char
    return result

def atbash(message): 
    lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
            'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
            'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
            'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
            'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'} 
    cipher = '' 
    for letter in message: 
        # checks for space 
        if(letter != ' '): 
            # adds the corresponding letter from the lookup_table 
            cipher += lookup_table.get(letter, letter)
        else: 
            # adds space 
            cipher += ' '
  
    return cipher

def affine(ciphered_text, a, b, m=26):
    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime. Please try again.')

    # msg = ''.join(x for x in ciphered_text if x.isalnum())
    msg = ciphered_text
    out = ''
    n = 1
    count = 1

    while True:
        if a*n > m*count:
            if a*n == (m*count) + 1:
                break
            count += 1
        n += 1

    for char in msg:
        if char.isalpha():
            d = int((n*(string.ascii_uppercase.index(char) - b)) % m)
            out += string.ascii_uppercase[d]
        else:
            out += char

    return out

def decryptFence(cipher, rails, offset=0, debug=False):
    plain = ''

    # offset
    if offset:
        t = encryptFence('o'*offset + 'x'*len(cipher), rails)
        for i in range(len(t)):
            if(t[i] == 'o'):
                cipher = cipher[:i] + '#' + cipher[i:]
    
    length = len(cipher)
    fence = [['#']*length for _ in range(rails)]

    # build fence
    i = 0
    for rail in range(rails):
        p = (rail != (rails-1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = cipher[i]
            if p:
                x += 2*(rails - rail - 1)
            else:
                x += 2*rail
            if (rail != 0) and (rail != (rails-1)):
                p = not p
            i += 1

    # print pretty fence
    if debug:
        printFence(fence)

    # read fence
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain

def decode(s):
    try:
        for i in range(26):
            dec = rot(enc, i)
            if is_flag(dec):
                return dec
    except:
        pass

    try:
        dec = base64.b64decode(enc).decode()
        if is_flag(dec):
            return dec
    except:
        pass
    try:
        dec = base64.b32decode(enc).decode()
        if is_flag(dec):
            return dec
    except:
        pass
    try:
        dec = base64.b16decode(enc).decode()
        if is_flag(dec):
            return dec
    except:
        pass

    try:
        dec = atbash(enc)
        if is_flag(dec):
            return dec
    except:
        pass

    try:
        dec = affine(enc, 9, 6)
        if is_flag(dec):
            return dec
    except:
        pass

    try:
        dec = decryptFence(enc, 3)
        if is_flag(dec):
            return dec
    except:
        pass
    
    return None


def is_flag(te, crib):
    return crib in flag.lower()

def main():
    r = remote('ctf.umbccd.io', 5200)
    r.recvlines(16)

    while True:
        enc = r.readline().decode().strip()
        dec = decode(enc)
        print(enc)
        print(dec)
        r.sendline(dec.encode())

if __name__ == '__main__':
    main()
