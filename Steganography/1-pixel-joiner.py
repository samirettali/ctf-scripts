#!/usr/bin/env python3
import io
from PIL import Image
import libarchive.public
from Crypto.Util.number import long_to_bytes

# This script opens a 7z archive containing a bunch of 1-pixel images and
# stiches them together forming one image.

colors = {}
test = b''
with libarchive.public.file_reader('chall.7z') as e:
    for entry in e:
        if entry.pathname.endswith('.jpg'):
            name = entry.pathname.split('/')[1].split('.')[0]
            file = bytes()
            for block in entry.get_blocks():
                file += block
            img = Image.open(io.BytesIO(file))
            colors[int(name)] = img.getpixel((0, 0))

img = Image.new(mode='RGB', size=(300, 300))
for name in sorted(colors.keys()):
    coords = long_to_bytes(name).decode().split()
    coords = (int(coords[0]), int(coords[1]))
    color = colors[name]
    img.putpixel(coords, color)
img.save('output.png')
