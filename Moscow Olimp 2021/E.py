#!/bin/pypy3
n = int(input())
to_leave = {1, 2, 3, n + 1, n + 2, 2 * n + 1}
all_elements = set([i for i in range(1, n ** 2 + 1)])
print(2, " ".join(map(str, all_elements - to_leave)))
del all_elements, to_leave
print(3, " ".join(map(str, {1, 3, 2 * n + 1})))
print(5, " ".join(map(str, {2, n + 1})))
