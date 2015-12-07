__author__ = 'Benny'

import sys

def skew(genome):
    sw = {}
    result = []

    i = 0
    sw[i] = 0
    for acid in genome.strip():
        if acid == 'C':
            sw[i+1] = sw[i] - 1
        elif acid == 'G':
            sw[i+1] = sw[i] + 1
        else:
            sw[i+1] = sw[i]
        i += 1
    minimo = min(sw.values())

    for j in sw:
        if sw[j] == minimo:
            result.append(j)
    return str(result).replace("[","").replace("]",'').replace(",",'')

lines = sys.stdin.read().splitlines()
print(skew(lines[0]))

'''d=open("Salmonella_enterica.txt").readlines()

#remove the header
d=d[1:-1]
print(skew("".join(map(str.strip, d))))
#[3764856, 3764858]

def strip1(t):
  return t.rstrip("\n")
print(skew("".join(map(strip1, d))))
#[3818639, 3818641]

def strip2(t):
  return t.rstrip("\r\n")
print(skew("".join(map(strip2, d))))
#[3764856, 3764858]'''

