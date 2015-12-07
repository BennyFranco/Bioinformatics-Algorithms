__author__ = 'Benny'

import numpy as np
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


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for text in dna:
        the_hamming_distance = 99999999
        for i in range(len(text)-k+1):
            if the_hamming_distance > hamming_distance(pattern, text[i:i+k]):
                the_hamming_distance = hamming_distance(pattern, text[i:i+k])
        distance = distance + the_hamming_distance
    return distance


def median_string(dna, k):
    distance = 9999999
    for i in range(4**k-1):
        pattern = number_to_pattern(i, k)
        if distance > distance_between_pattern_and_strings(pattern, dna):
            distance = distance_between_pattern_and_strings(pattern, dna)
            median = pattern
    return median

f = sys.stdin.read().splitlines()
#k = int(f[0])

#dna_list = [line.strip() for line in f]
#dna_list.pop(0)

#motifs = median_string(dna_list, k)
tr = str(f[1])

print(distance_between_pattern_and_strings(f[0],tr.split(' ')))