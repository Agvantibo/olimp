#!/bin/python3
a, b, c = [int(i) for i in input().split()]

if ((a + b + c) / 3) % 1 != 0:
    print('IMPOSSIBLE')
else:
    seq = [a, b, c]
    seq.sort()
    print(seq[-1] - seq[1])
