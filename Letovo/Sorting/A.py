#!/bin/pypy3
int(input())
r = [int(i) for i in input().split()]
buf = max(r)
r[r.index(buf)] = r[0]
r[0] = buf

print(" ".join(map(str, r)))
