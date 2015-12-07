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
lines = sys.stdin.read().splitlines()

print(pattern_to_number(lines[0]))