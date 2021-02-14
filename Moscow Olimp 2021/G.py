#!/bin/pypy3
from math import ceil
parties, N_bulletins = [int(i) for i in input().split()]
bulletins = []

for i in range(N_bulletins):
    proc = input()
    if '+' in proc:
        if proc.count('+') == 1:
            bulletins.append(proc)
del proc
del N_bulletins

partyVotes = [0 for i in range(parties)]
for i in bulletins:
    partyVotes[i.index("+")] += 1
del bulletins

total = 0
for i in partyVotes:
    total += i

for i in range(parties):
    partyVotes[i] = ceil(partyVotes[i] / (total / 100))

to_print = ''
for i in range(parties):
    if partyVotes[i] >= 7:
        to_print += str(i + 1) + " "

del parties
del partyVotes
print(to_print)
