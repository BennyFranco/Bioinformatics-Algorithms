__author__ = 'Benny'

import sys

def symbol_to_number(symbol):
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

def computing_frequencies(text, k):
    frequency_array = [0]*(4**k)

    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array


def better_clump_finding(genome, k, l, t):
        frequent_patterns = []
        clump = [0]*(4**k)

        if len(genome) <= 8:
            text = genome[0:]
        else:
            text = genome[0:l]
        frequency_array = computing_frequencies(text, k)

        for i in range((4**k)):
            if frequency_array[i] >= t:
                clump[i] = 1

        for i in range(len(genome)-l):
            first_pattern = genome[i:k+i]
            index = pattern_to_number(first_pattern)

            frequency_array[index] -= 1
            last_pattern = genome[i + l - k:i + l]

            index = pattern_to_number(last_pattern)
            frequency_array[index] += 1

            if frequency_array[index] >= t:
                clump[index] = 1

        for i in range((4**k)):
            if clump[i] == 1:
                pattern = number_to_pattern(i, k)
                frequent_patterns.append(pattern)

        return frequent_patterns

lines = sys.stdin.read().splitlines()
text1 = lines[0]
ttext = str(lines[1])
ttext = ttext.split(' ')
k1 = int(ttext[0])
l1 = int(ttext[1])
t1 = int(ttext[2])

print(' '.join(better_clump_finding(text1, k1, l1, t1)))