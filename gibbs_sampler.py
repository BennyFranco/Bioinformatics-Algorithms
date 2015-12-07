__author__ = 'Benny'

from random import randint
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


def profile_with_pseudocounts(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)+1) / float(len(col)+4) for nuc in 'ACGT'] for col in columns]


def score(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count


def motifs_from_profile(profile, dna, k):
    return [profile_most_probable_kmer(seq, k, profile) for seq in dna]


def gibbs_sampler(dna, k, t, n):
    rand_ints = [randint(0,len(dna[0])-k) for a in range(t)]
    motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]

    best_score = [score(motifs), motifs]

    for i in range(n):
        r = randint(0,t-1)
        current_profile = profile_with_pseudocounts([motif for index, motif in enumerate(motifs) if index!=r])
        motifs = [profile_most_probable_kmer(dna[index],k,current_profile) if index == r else motif for index,motif in enumerate(motifs)]
        current_score = score(motifs)
        if current_score < best_score[0]:
            best_score = [current_score, motifs]
    return best_score


f = sys.stdin.read().splitlines()
k, t, n = map(int, str(f[0]).split(' '))

dna_list = [line.strip() for line in f]
dna_list.pop(0)

best_motifs = [k*t, None]

for repeat in range(20):
    current_motifs = gibbs_sampler(dna_list,k,t,n)
    if current_motifs[0] < best_motifs[0]:
        best_motifs = current_motifs

print('\n'.join(best_motifs[1]))
