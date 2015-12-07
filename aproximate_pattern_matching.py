__author__ = 'Benny'

import sys

def hamming_distance(p, q):
    dif = 0
    for i in range(len(p)):
        if not q[i] == p[i]:
            dif += 1
    return dif


def pattern_matching(pattern, text, d):
    string_pos = []

    for i in range(len(text) - len(pattern) + 1):
        pattern_prima = text[i:len(pattern)+i]
        if hamming_distance(pattern,pattern_prima) <= d:
            string_pos.append(i)

    return str(string_pos).replace("[", "").replace("]", '').replace(",", '')

lines = sys.stdin.read().splitlines()
print(pattern_matching(lines[0], lines[1], int(lines[2])))