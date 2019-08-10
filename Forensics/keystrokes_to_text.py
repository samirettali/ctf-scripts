#!/usr/bin/env python3
from sys import argv


# This script reads keystrokes extracted from pcap files and reconstructs the
# input. The command to extract the keystrokes is:
# tshark -r deadly_arthropod.pcap -T fields -e usb.capdata | awk 'NF' > keystrokes.txt


def main():
    if len(argv) != 2:
        print('Usage: %s <keycodes_file>' % argv[0])
        exit(1)

    f = open(argv[1], 'r')

    keymap = {
        '01': 'MOD_LCTRL',
        '02': 'MOD_LSHIFT',
        '04': 'MOD_LALT',
        '08': 'MOD_LMETA',
        '10': 'MOD_RCTRL',
        '20': 'MOD_RSHIFT',
        '40': 'MOD_RALT',
        '80': 'MOD_RMETA',
        '00': 'NONE',
        '01': 'ERR_OVF',
        '04': 'A',
        '05': 'B',
        '06': 'C',
        '07': 'D',
        '08': 'E',
        '09': 'F',
        '0a': 'G',
        '0b': 'H',
        '0c': 'I',
        '0d': 'J',
        '0e': 'K',
        '0f': 'L',
        '10': 'M',
        '11': 'N',
        '12': 'O',
        '13': 'P',
        '14': 'Q',
        '15': 'R',
        '16': 'S',
        '17': 'T',
        '18': 'U',
        '19': 'V',
        '1a': 'W',
        '1b': 'X',
        '1c': 'Y',
        '1d': 'Z',
        '1e': '1',
        '1f': '2',
        '20': '3',
        '21': '4',
        '22': '5',
        '23': '6',
        '24': '7',
        '25': '8',
        '26': '9',
        '27': '0',
        '28': '↲',
        '29': 'ESC',
        '2a': 'BACKSPACE',
        '2b': 'TAB',
        '2c': ' ',
        '2d': '-',
        '2e': '=',
        '2f': '{',
        '30': '}',
        '31': 'BACKSLASH',
        '32': 'HASHTILDE',
        '33': ':',
        '34': '\'',
        '35': 'GRAVE',
        '36': ',',
        '37': '.',
        '38': '/',
        '39': 'CAPSLOCK',
        '3a': 'F1',
        '3b': 'F2',
        '3c': 'F3',
        '3d': 'F4',
        '3e': 'F5',
        '3f': 'F6',
        '40': 'F7',
        '41': 'F8',
        '42': 'F9',
        '43': 'F10',
        '44': 'F11',
        '45': 'F12',
        '46': 'SYSRQ',
        '47': 'SCROLLLOCK',
        '48': 'PAUSE',
        '49': 'INSERT',
        '4a': 'HOME',
        '4b': 'PAGEUP',
        '4c': 'DELETE',
        '4d': 'END',
        '4e': 'PAGEDOWN',
        '4f': '→',
        '50': '←',
        '51': '↓',
        '52': '↑',
        '53': 'NUMLOCK',
        '54': 'KPSLASH',
        '55': 'KPASTERISK',
        '56': 'KPMINUS',
        '57': 'KPPLUS',
        '58': 'KPENTER',
        '59': 'KP1',
        '5a': 'KP2',
        '5b': 'KP3',
        '5c': 'KP4',
        '5d': 'KP5',
        '5e': 'KP6',
        '5f': 'KP7',
        '60': 'KP8',
        '61': 'KP9',
        '62': 'KP0',
        '63': 'KPDOT',
        '64': '102ND',
        '65': 'COMPOSE',
        '66': 'POWER',
        '67': 'KPEQUAL',
        '68': 'F13',
        '69': 'F14',
        '6a': 'F15',
        '6b': 'F16',
        '6c': 'F17',
        '6d': 'F18',
        '6e': 'F19',
        '6f': 'F20',
        '70': 'F21',
        '71': 'F22',
        '72': 'F23',
        '73': 'F24',
        '74': 'OPEN',
        '75': 'HELP',
        '76': 'PROPS',
        '77': 'FRONT',
        '78': 'STOP',
        '79': 'AGAIN',
        '7a': 'UNDO',
        '7b': 'CUT',
        '7c': 'COPY',
        '7d': 'PASTE',
        '7e': 'FIND',
        '7f': 'MUTE',
        '80': 'VOLUMEUP',
        '81': 'VOLUMEDOWN',
        '85': 'KPCOMMA',
        '87': 'RO',
        '88': 'KATAKANAHIRAGANA',
        '89': 'YEN',
        '8a': 'HENKAN',
        '8b': 'MUHENKAN',
        '8c': 'KPJPCOMMA',
        '90': 'HANGEUL',
        '91': 'HANJA',
        '92': 'KATAKANA',
        '93': 'HIRAGANA',
        '94': 'ZENKAKUHANKAKU',
        'b6': 'KPLEFTPAREN',
        'b7': 'KPRIGHTPAREN',
        'e0': 'LEFTCTRL',
        'e1': 'LEFTSHIFT',
        'e2': 'LEFTALT',
        'e3': 'LEFTWINDOWS',
        'e4': 'RIGHTCTRL',
        'e5': 'RIGHTSHIFT',
        'e6': 'RIGHTALT',
        'e7': 'RIGHTMETA',
        'e8': 'MEDIA_PLAYPAUSE',
        'e9': 'MEDIA_STOPCD',
        'ea': 'MEDIA_PREVIOUSSONG',
        'eb': 'MEDIA_NEXTSONG',
        'ec': 'MEDIA_EJECTCD',
        'ed': 'MEDIA_VOLUMEUP',
        'ee': 'MEDIA_VOLUMEDOWN',
        'ef': 'MEDIA_MUTE',
        'f0': 'MEDIA_WWW',
        'f1': 'MEDIA_BACK',
        'f2': 'MEDIA_FORWARD',
        'f3': 'MEDIA_STOP',
        'f4': 'MEDIA_FIND',
        'f5': 'MEDIA_SCROLLUP',
        'f6': 'MEDIA_SCROLLDOWN',
        'f7': 'MEDIA_EDIT',
        'f8': 'MEDIA_SLEEP',
        'f9': 'MEDIA_COFFEE',
        'fa': 'MEDIA_REFRESH',
        'fb': 'MEDIA_CALC',
    }

    result = ''
    for line in f:
        modifier = line[0:2]
        key = line[4:6]
        if key != '00':
            if modifier == '02' or modifier == '20':
                result += keymap.get(key).upper()
            else:
                result += keymap.get(key).lower()

    final_string = ''
    index = 0
    for c in result:
        if c != '←' and c != '→':
            if c == '↲':
                c = '\n'
            final_string = final_string[:index] + c + final_string[index:]
            index += 1
        elif c == '←':
            index -= 1
        elif c == '→':
            index += 1
    print('Complete input\n')
    print(result)
    print('\nFinal input\n')
    print(final_string)


if __name__ == '__main__':
    main()
