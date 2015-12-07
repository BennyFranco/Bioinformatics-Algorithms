__author__ = 'Benny'

import re
import sys

def pattern_match(pattern, text):
    result = ''
    pattern = '(?='+pattern+')'

    for a in [m.start() for m in re.finditer(pattern, text)]:
        result += str(a) + ' '

    return result

lines = sys.stdin.read().splitlines()

print(pattern_match(lines[0], lines[1]))
