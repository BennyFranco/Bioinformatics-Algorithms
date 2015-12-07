__author__ = 'Benny'

import sys

def hamming_distance(p, q):
    dif = 0
    for i in range(len(p)):
        if not q[i] == p[i]:
            dif += 1
    return dif

def approximate_pattern_count(pattern, text, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        pattern_prima = text[i:i + len(pattern)]
        if hamming_distance(pattern, pattern_prima) <= d:
            count += 1
    return count


lines = sys.stdin.read().splitlines()
print(approximate_pattern_count(lines[0], lines[1], int(lines[2])))
