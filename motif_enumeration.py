__author__ = 'Benny'

import re
import sys


def symbol_to_number(symbol):
    pass
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3


def number_to_symbol(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'


def quotient(index):
    return index // 4


def remainder(index):
    return index % 4


def pattern_to_number(pattern):
    if pattern == '':
        return 0

    symbol = pattern[len(pattern) - 1]
    prefix = pattern[:len(pattern) - 1]

    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)

    prefix_index = quotient(index)
    r = remainder(index)

    symbol = number_to_symbol(r)

    prefix_pattern = number_to_pattern(prefix_index, k - 1)

    return prefix_pattern + symbol


def hamming_distance(p, q):
    dif = 0
    for i in range(len(p)):
        if not q[i] == p[i]:
            dif += 1
    return dif


def neighbors(pattern, d):
    alt_bases = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
    suffix = pattern[1:]
    neighborhood = []

    if d == 0:
        neighborhood.append(pattern)
        return neighborhood

    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    suffix_neighbors = neighbors(suffix, d)
    for st in suffix_neighbors:
        if hamming_distance(suffix, st) < d:
            for nucleotide_x in alt_bases:
                neighborhood.append(nucleotide_x + st)
        else:
            neighborhood.append(pattern[0] + st)
    return neighborhood


def approximate_pattern_count(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        pattern_prima = text[i:i + len(pattern)]
        if hamming_distance(pattern, pattern_prima) <= d:
            count += 1
    return count


def motif_enumeration(dna, k, d):
    patterns = []
    temp = []
    for pattern in dna:
        for i in range(len(pattern)-k+1):
            for kmer_prima in neighbors(pattern[i:k+i],d):
                for tp in dna:
                    if approximate_pattern_count(tp,kmer_prima,d) > 0:
                        temp.append(kmer_prima)
                if len(temp) == len(dna):
                    if patterns.count(kmer_prima) < 1:
                        patterns.append(kmer_prima)
                temp = []
    return sorted(patterns)

f = sys.stdin.read().splitlines()
k, d = map(int, str(f[0]).split(" "))

dna_list = [line.strip() for line in f]
dna_list.pop(0)

motifs = motif_enumeration(dna_list, k, d)

print(' '. join(motifs))
