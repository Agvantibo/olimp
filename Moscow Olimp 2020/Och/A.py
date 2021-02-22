#!/bin/pypy3
a, b, n, k, = int(input()), int(input()), int(input()), int(input())


def foo(a, b):
    if a % 2 == 0 and b % 2 == 0 and b <= a:
        return 0
    elif a % 2 == 0 and b % 2 == 0:
        return b - a
    else:
        return b + 1


print(a + 1 + foo(a, b) * k + foo(b, a) * (k - 1) + foo(b, n))
