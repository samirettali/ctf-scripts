#!/usr/bin/env python3
from PIL import Image
import requests
import urllib
from bs4 import BeautifulSoup
from sys import argv

# This script solves level 26 from 0xf.at.
# It fetches the given image and for every row calculates the offset of the first non white pixel.
# The offset represents a letter from the alphabet.
# The password for the level is given by all the letters found in the image.
def main():
    s = requests.Session()
    cookies = {'PHPSESSID': 'damnsdfemhble4gl7r3h2i8ml1'}
    url = 'https://www.0xf.at/play/26'
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text, 'html.parser')
    for img in soup.select('img'):
        if 'data/tmp' in img['src']:
            image_url = 'https://www.0xf.at' + img['src']
            image = requests.get(image_url, cookies=cookies, stream=True).raw
            image = Image.open(image).convert('RGB')
            pixels = image.load()
            w, h = image.size
            password = ''
            for j in range(h):
                for i in range(w):
                    if pixels[i, j] != (255, 255, 255):
                        password += chr(ord('a') + i)
            requests.get(url + '?pw=' + password, cookies=cookies)
            break


if __name__ == '__main__':
    main()
