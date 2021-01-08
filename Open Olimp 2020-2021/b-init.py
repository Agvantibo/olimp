#!/bin/python3
from math import ceil

n, m, k = [int(i) for i in input().split()]
# n - jobs, m - tutors, k - passes

Teachers = [i + 1 for i in range(m)]
JobStatus = [k for i in range(n)]
hours = ceil(k * n / m)
Jobs = [[0 for j in range(n)] for i in range(hours)]
tc = -2


def get_teacher(cur, length):
    return Teachers[cur % length]


for i in range(hours):
    tc += 1
    ut = 0
    for j in range(n):
        if JobStatus[j] != 0:
            tc += 1
            ut += 1
            JobStatus[j] -= 1
            Jobs[i][j] = get_teacher(tc, m)
            if ut == m:
                break

print(hours)
for i in Jobs:
    print(" ".join(map(str, i)))
