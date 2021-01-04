#!/bin/python3
from math import ceil

n, m, k = [int(i) for i in input().split()]
# n - jobs, m - tutors, k - passes

Teachers = [i + 1 for i in range(m)]
JobStatus = [k for i in range(n)]
Hours = ceil(k * n / m)
Jobs = [[0 for j in range(n)] for i in range(Hours)]
LockedTeachers = []


def write_teacher(i1, i2):
    for a in range(m):
        if LockedTeachers[a] == 0:
            if i == 0:
                LockedTeachers[a] = 1
                Jobs[i1][i2] = Teachers[a]
            elif Teachers[a] == Jobs[i1-1][i2]:
                continue


for i in range(Hours):
    ut = 0
    LockedTeachers = [0 for f in range(m)]
    for j in range(n):
        if JobStatus[j] > 0:
            if ut == m:
                break
            else:
                ut += 1
                write_teacher(i, j)


print(Hours)
for i in Jobs:
    print(" ".join(map(str, i)))
