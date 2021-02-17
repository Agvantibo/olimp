#!/bin/pypy3

input()
data = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()]

for i in queries:
    if i in data:
        print("YES")
    else:
        print("NO")
