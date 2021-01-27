#!/bin/pypy3
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
    total += 1

for i in range(parties):
    partyVotes[i] = partyVotes[i] + 1 // total - 1

for i in range(parties):
    if partyVotes[i] > 17:
        print(i + 1)
