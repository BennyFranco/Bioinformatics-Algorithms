__author__ = 'Benny'

import sys

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

    return patterns[max(patterns)]


def score(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count


def profile(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'] for col in columns]


def greedy_motif_search(dna_list, k, t):
    best_score = t*k

    for i in range(len(dna_list[0])-k+1):
        motifs = [dna_list[0][i:i+k]]

        for j in range(1, t):
            current_profile = profile(motifs)
            motifs.append(profile_most_probable_kmer(dna_list[j], k, current_profile))

        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


def profile_with_pseudocounts(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)+1) / float(len(col)+4) for nuc in 'ACGT'] for col in columns]


def greedy_motif_search_pseudocounts(dna_list, k, t):
    best_score = t*k

    for i in range(len(dna_list[0]) - k + 1):
        motifs = [dna_list[0][i:i + k]]

        for j in range(1, t):
            current_profile = profile_with_pseudocounts(motifs)
            motifs.append(profile_most_probable_kmer(dna_list[j], k, current_profile))

        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs

f = sys.stdin.read().splitlines()
k, d = map(int, str(f[0]).split(" "))

dna_list = [line.strip() for line in f]
dna_list.pop(0)

motifs = greedy_motif_search_pseudocounts(dna_list, k, d)

print('\n'.join(motifs))