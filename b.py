#!/bin/python3
from math import ceil

TotalJobs, TotalTeachers, Passes = [int(i) for i in input().split()]
Hours = ceil(Passes * TotalJobs / TotalTeachers)
Jobs = [[0 for j in range(TotalJobs)] for i in range(Hours)]
UsedTeachers = 0

for i in range(TotalJobs):
    UsedTeachers += 1
    Jobs[0][i] = i + 1
    if UsedTeachers == TotalTeachers:
        break

for i in range(1, Hours):
    for j in range(TotalJobs - 1):
        Jobs[i][j] = Jobs[i - 1][j + 1]
    Jobs[i][-1] = Jobs[i - 1][0]

print(Hours)
for i in Jobs:
    print(" ".join(map(str, i)))
