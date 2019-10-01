#!/usr/bin/env python3
import struct
import zlib
from binascii import hexlify, unhexlify
from difflib import get_close_matches
from sys import argv

CHUNK_TYPES = ['IHDR', 'PLTE', 'IDAT', 'bKGD', 'cHRM', 'dSIG', 'eXIf', 'gAMA',
               'hIST', 'iCCP', 'iTXt', 'pHYs', 'sBIT', 'sPLT', 'sRGB', 'sTER',
               'tEXt', 'tIME', 'tRNS', 'zTXt']


out_file = None


def hex_int(b):
    return struct.unpack('>I', b)[0]


def fix(filename):
    global out_file
    f = open(filename, 'rb')

    PNG_HEADER = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

    # Header
    header = f.read(8)
    if header != PNG_HEADER:
        header = PNG_HEADER
        print('[*] Replacing PNG header\n')

    out_file.write(header)
    check_chunk(f)
    check_chunk(f)
    check_chunk(f)
    check_chunk(f)
    check_chunk(f)
    out_file.write(unhexlify(hex(0x49454e44ea426028)[2:]))


def get_correct_type(t):
    match = get_close_matches(t, CHUNK_TYPES, len(CHUNK_TYPES), 0)
    if isinstance(match, list):
        match = match[0]
    return match


def check_chunk(f, length=None):
    global out_file

    # Reading chunk parts
    if not length:
        length = f.read(4)
    chunk_type = f.read(4)
    data = f.read(hex_int(length))
    crc = f.read(4)

    print('[*] Analyzing %s chunk of length %d' % (chunk_type, hex_int(length)))
    if crc == struct.pack('!I', zlib.crc32(chunk_type + data) & 0xffffffff):
        print('    This chunk seems fine')
    else:
        print('    This chunk is corrupted')

        # Analyzing chunk data
        if len(data) != hex_int(length):
            print('    The length of the chunk is wrong')
            print('    This chunk is going to be recomputed\n')
            correct_length = data.index('IEND'.encode()) - 4
            f.seek(-len((chunk_type + data + crc)), 1)
            check_chunk(f, unhexlify(hex(correct_length)[2:].zfill(8)))
            return

        # Analyzing chunk header
        correct_chunk_type = get_correct_type(chunk_type)
        if chunk_type == correct_chunk_type:
            print('    The type is valid')
        else:
            print('    The type is not valid, probably %s' % (correct_chunk_type))
            chunk_type = correct_chunk_type

        print('    Recomputing CRC')
        crc = struct.pack('!I', zlib.crc32(chunk_type + data) & 0xffffffff)

    chunk = length + chunk_type + data + crc
    out_file.write(chunk)

    print('')

def main():
    if len(argv) != 3:
        print('Usage: ./%s <file> <output>' % argv[0])
        exit(1)

    global out_file

    for i in range(len(CHUNK_TYPES)):
        CHUNK_TYPES[i] = CHUNK_TYPES[i].encode()

    out_file = open(argv[2], 'wb')
    fix(argv[1])
    print('Fixing done')

if __name__ == '__main__':
    main()
