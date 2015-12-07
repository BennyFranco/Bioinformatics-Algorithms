__author__ = 'Benny'

import numpy as np
import sys


def profile_most_probable(text, k, matrix):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}

    list_string = []
    current_probability = 0
    patterns = {}

    for i in range(len(text)-k+1):
        list_string.append(text[i:i+k])

    for pattern in list_string:
        for j, nucleotide in enumerate(pattern):
            current_probability += matrix[j][nuc_loc[nucleotide]]
        patterns[current_probability] = pattern
        current_probability = 0

    return patterns


def profile_most_probable_kmer(dna, k, profile):
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}

    max_probability = -1

    for i in range(len(dna)-k+1):
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]

        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable



f = sys.stdin.read().splitlines()
k = int(f[1])
text_dna = f[0]

f[0]=''
f[1]=''

profile_m = np.loadtxt(f, unpack=True, delimiter=' ')

print(profile_most_probable_kmer(text_dna,k,profile_m))