__author__ = 'Benny'

import sys

def hamming_distance(p,q):
    dif = 0
    for i in range(len(p)):
        if not q[i] == p[i]:
            dif += 1
    return dif

lines = sys.stdin.read().splitlines()
print(hamming_distance(lines[0], lines[1]))