#!/usr/bin/env python3


"""
Build string to solve misDIRection HackTheBox challenge
Example:
secret$ tree
.
├── 0
│   └── 6
├── 1
│   ├── 22
│   └── 30
├── 2
│   └── 34
├── 3
├── 4
├── 5
│   └── 16
├── 6
├── 7
├── 8
├── 9
│   └── 36
├── A
├── B
│   └── 23
├── F
│   ├── 19
│   ├── 2
│   └── 27
├── H
├── N
│   ├── 11
│   ├── 25
│   ├── 31
│   └── 33
├── P
│   └── 32
├── S
│   ├── 1
│   └── 24
├── U
│   ├── 20
│   ├── 28
│   └── 9
├── V
│   └── 35
├── W
├── X
│   ├── 15
│   ├── 17
│   ├── 21
│   └── 29
├── c
│   └── 4
├── d
│   ├── 13
│   └── 26
├── e
│   ├── 14
│   └── 5
├── g
├── i
├── j
│   ├── 10
│   ├── 12
│   └── 8
├── k
├── l
├── m
├── o
├── q
├── r
│   ├── 3
│   └── 7
├── t
├── y
└── z
    └── 18

36 directories, 36 files

secret$python misdirection.py .
      r
  r   r
  r   r            U
  r   r U          U
  r   r U          U       U
  r   r U          U       U       9
  r  0r U          U       U       9
  r  0r U          U       U    N  9
  r  0r U N        U       U    N  9
  r  0r U N        U       U  N N  9
  r  0r U N        U    N  U  N N  9
  r  0r U N      z U    N  U  N N  9
  r  0r U N      z U    N  U 1N N  9
  r  0r U N      z U 1  N  U 1N N  9
S r  0r U N      z U 1  N  U 1N N  9
S r  0r U N      z U 1 SN  U 1N N  9
S r  0r U N      z U 1 SN FU 1N N  9
S r  0r U N      zFU 1 SN FU 1N N  9
SFr  0r U N      zFU 1 SN FU 1N N  9
SFr  0r UjN      zFU 1 SN FU 1N N  9
SFr  0rjUjN      zFU 1 SN FU 1N N  9
SFr  0rjUjNj     zFU 1 SN FU 1N N  9
SFrc 0rjUjNj     zFU 1 SN FU 1N N  9
SFrc 0rjUjNj     zFU 1 SNdFU 1N N  9
SFrc 0rjUjNjd    zFU 1 SNdFU 1N N  9
SFrc 0rjUjNjd    zFU 1 SNdFU 1N N V9
SFrc 0rjUjNjd    zFU 1 SNdFUX1N N V9
SFrc 0rjUjNjd   XzFU 1 SNdFUX1N N V9
SFrc 0rjUjNjd   XzFUX1 SNdFUX1N N V9
SFrc 0rjUjNjd X XzFUX1 SNdFUX1N N V9
SFrce0rjUjNjd X XzFUX1 SNdFUX1N N V9
SFrce0rjUjNjdeX XzFUX1 SNdFUX1N N V9
SFrce0rjUjNjdeX XzFUX1BSNdFUX1N N V9
SFrce0rjUjNjdeX XzFUX1BSNdFUX1N N2V9
SFrce0rjUjNjdeX5XzFUX1BSNdFUX1N N2V9
SFrce0rjUjNjdeX5XzFUX1BSNdFUX1NPN2V9
SFrce0rjUjNjdeX5XzFUX1BSNdFUX1NPN2V9
"""


import os
from sys import argv


if len(argv) != 2:
    print('Usage: ./%s <directory>' % argv[0])
    exit(1)

working_directory = argv[1]
directories = os.listdir(working_directory)

characters = []
# Loop through directories
for directory in directories:
    if os.path.isdir(os.path.join(os.path.abspath(working_directory), directory)):
        filenames = os.listdir(directory)
        # Loop through files inside the directory
        for filename in filenames:
            index = int(filename) - 1
            # Expand characters array up to the index size
            for i in range(index - len(characters) + 1):
                characters.append(' ')
            characters[index] = directory
            print(''.join(characters))
print(''.join(characters))
