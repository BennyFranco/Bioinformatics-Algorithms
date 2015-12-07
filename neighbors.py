__author__ = 'Benny'

import sys


def hamming_distance(p, q):
    dif = 0
    for i in range(len(p)):
        if not q[i] == p[i]:
            dif += 1
    return dif


def neighbors(pattern, d):
    alt_bases = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
    suffix = pattern[1:]

    if d == 0:
        return pattern

    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    neighborhood = []
    suffix_neighbors = neighbors(suffix, d)
    for st in suffix_neighbors:
        if hamming_distance(suffix, st) < d:
            for nucleotide_x in alt_bases:
                neighborhood.append(nucleotide_x + st)
        else:
            neighborhood.append(pattern[0] + st)
    return neighborhood

lines = sys.stdin.read().splitlines()
print('\n'.join(neighbors(lines[0], int(lines[1]))))