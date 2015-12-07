__author__ = 'Benny'
import sys

def reverse_complement(pattern):
    complement = []

    for acid in pattern:
        if acid == 'A':
            acid = 'T'
        elif acid == 'T':
            acid = 'A'
        elif acid == 'G':
            acid = 'C'
        else:
            acid = 'G'

        complement.append(str(acid))

    complement.reverse()

    return complement

lines = sys.stdin.read().splitlines()

print(''.join(reverse_complement(lines[0])))
