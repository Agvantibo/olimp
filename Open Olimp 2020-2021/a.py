#!/bin/python3
n, a, x, m = int(input()), int(input()), int(input()), int(input())
litres = ((n * a) - x) // m
if litres <= 0:
    print(0)
else:
    print(litres)
