#!/bin/pypy3
input()
keys = [int(i) for i in input().split()]
input()
key_presses = [int(i) for i in input().split()]

for i in key_presses:
    keys[i - 1] -= 1

for i in keys:
    if i < 0:
        print('yes')
    else:
        print('no')
