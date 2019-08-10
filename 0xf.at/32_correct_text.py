#!/usr/bin/env python3
import requests
import difflib
from bs4 import BeautifulSoup
from sys import argv

def main():
    s = requests.Session()
    cookies = {'PHPSESSID': 'damnsdfemhble4gl7r3h2i8ml1'}
    url = 'https://www.0xf.at/play/32'
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text, 'html.parser')

    text = soup.find('blockquote').text
    text = text.replace('.', '')
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('\r', '')
    text = text.upper()
    text = text.split(' ')
    dictionary = open('latindictionary.txt').read().upper().split('\n')[:-1]

    password = ''
    for word in text:
        correct = difflib.get_close_matches(word, dictionary, n=1)[0]
        if word != correct and len(word) == len(correct):
            print(word, correct)
            for i in range(len(word)):
                if word[i] != correct[i]:
                    first_char = ord(word[i]) - ord('A')
                    second_char = ord(correct[i]) - ord('A')
                    difference = (first_char - second_char)
                    print(word[i]  + ' -> ' + correct[i])
                    if difference == 1:
                        password += correct[i]
    print(password)
    requests.get(url + '?pw=' + password, cookies=cookies).text



if __name__ == '__main__':
    main()
