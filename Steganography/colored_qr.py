#!/usr/bin/env python3

"""
This script reads a colored qr code and tries all the black/white combinations
until a valid one is found
Used to solve PRISM challenge from InnoCTF 2019
"""

import string
import random
from PIL import Image
from itertools import combinations


def main():
    img = Image.open('prism.png')

    w, h = img.size

    white = (255, 255, 255)
    black = (0, 0, 0)

    new_image = Image.new(img.mode, img.size)
    new = new_image.load()

    data = img.load()

    seen_colors = []

    for x in range(w):
        for y in range(h):
            color = data[x, y]
            if color not in seen_colors:
                seen_colors.append(color)

    seen_colors.remove(white)
    seen_colors.remove(black)

    for i in range(len(seen_colors)):
        potential = combinations(seen_colors, i + 1)

        for good in potential:
            for x in range(w):
                for y in range(y):
                    color = data[x, y]

                    if color == black or color == white:
                        new[x, y] = color

                    elif color in good:
                        new[x, y] = black
                    else:
                        new[x, y] = white

        new_image.save(''.join([random.choice(string.ascii_lowercase)
                       for _ in range(10)])) + '.png'


if __name__ == '__main__':
    main()
