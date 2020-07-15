#!/usr/bin/env python3
import hgtk

# This script decodes Standard Korean Alphabet Transliteration System (SKATS)
# morse from Korean.

translation = {
   'L':  'ㄱ',
   'F':  'ㄴ',
   'B':  'ㄷ',
   'V':  'ㄹ',
   'M':  'ㅁ',
   'W':  'ㅂ',
   'G':  'ㅅ',
   'K':  'ㅇ',
   'P':  'ㅈ',
   'C':  'ㅊ',
   'X':  'ㅋ',
   'Z':  'ㅌ',
   'O':  'ㅍ',
   'J':  'ㅎ',
   'E':  'ㅏ',
   'I':  'ㅑ',
   'T':  'ㅓ',
   'S':  'ㅕ',
   'A':  'ㅗ',
   'N':  'ㅛ',
   'H':  'ㅜ',
   'R':  'ㅠ',
   'D':  'ㅡ',
   'U':  'ㅣ',
}
priority = {
   'TU': 'ㅔ',
   'EU': 'ㅐ',
   'SU': 'ㅖ',
   'IU': 'ㅒ'
}

phrase = 'j  d  u    m  e  k     k  d  f     p  u  f     p  t  k    j  e  f    l  u    g  e  u  k    c  h  k    k  u  w   f  u    b  e'
for word in phrase.upper().split('   '):
    try:
        for char in priority.keys():
            word = word.replace(char, priority[char])

        for char in translation.keys():
            word = word.replace(char, translation[char])
        w = word.split()
        hangul = hgtk.letter.compose(*w)
        print(hangul, word)
    except:
        print(word)
        pass
