#!/usr/bin/env python3
from PIL import Image
from bs4 import BeautifulSoup
import requests
import pytesseract


# This script solves level 30 from 0xf.at.
# It fetches the image and splits it into 6x5 blocks and sorts them by color


def main():
    s = requests.Session()
    cookies = {'PHPSESSID': 'damnsdfemhble4gl7r3h2i8ml1'}
    url = 'https://www.0xf.at/play/30'
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text, 'html.parser')
    image = None
    for img in soup.select('img'):
        if 'data/tmp' in img['src']:
            image_url = 'https://www.0xf.at' + img['src']
            image = requests.get(image_url, cookies=cookies, stream=True).raw
            image = Image.open(image).convert('RGBA')
            break

    rows = 5
    cols = 6
    size = int(image.size[0] / cols)
    sorted_image = Image.new('RGBA', image.size)
    blocks = []
    for r in range(rows):
        for c in range(cols):
            box = (c * size, r * size, (c+1) * size, (r+1) * size)
            block = image.crop(box)
            angle = block.load()[0, 0]
            blocks.append((block, angle[1]))
    blocks = sorted(blocks, key=lambda x: x[1], reverse=True)

    for r in range(rows):
        for c in range(cols):
            box = (c * size, r * size, (c+1) * size, (r+1) * size)
            sorted_image.paste(blocks[0][0], box)
            blocks.remove(blocks[0])
    sorted_image.show()


if __name__ == '__main__':
    main()
