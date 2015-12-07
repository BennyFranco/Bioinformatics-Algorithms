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
    frequency_array = {}
    keys = {}

    for i in range(len(text)-k+1):
            pattern = text[i:i+k]
            j = pattern_to_number(pattern)
            if keys.get(j):
                frequency_array[j] += 1
            else:
                frequency_array[j] = 1
                keys[j]=j
    return frequency_array

def faster_frequent_words(text, k):
        frequent_patterns = []
        frequency_array = computing_frequencies(text, k)
        max_count = max(frequency_array.values())

        for i in frequency_array:
                if frequency_array[i] == max_count:
                    pattern = number_to_pattern(i, k)
                    frequent_patterns.append(pattern)
        return frequent_patterns

lines = sys.stdin.read().splitlines()

print(' '.join(faster_frequent_words(lines[0], int(lines[1]))))