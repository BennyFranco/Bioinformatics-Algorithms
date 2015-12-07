__author__ = 'Benny'

import sys

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

lines = sys.stdin.read().splitlines()  # read in the input from STDIN

print(pattern_count(lines[0],lines[1]))
#print(pattern_count('GCGCG','GCG'))