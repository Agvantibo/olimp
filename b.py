#!/bin/python3
from math import ceil

TotalJobs, TotalTeachers, Passes = [int(i) for i in input().split()]

Teachers = [i + 1 for i in range(TotalTeachers)]
JobStatus = [Passes for i in range(TotalJobs)]
Hours = ceil(Passes * TotalJobs / TotalTeachers)
Jobs = [[0 for j in range(TotalJobs)] for i in range(Hours)]
LockedTeachers = []


def write_teacher(i1, i2):
    for a in range(TotalTeachers):
        if LockedTeachers[a] == 0:
            if i == 0:
                LockedTeachers[a] = 1
                Jobs[i1][i2] = Teachers[a]
            elif Teachers[a] == Jobs[i1-1][i2]:
                continue


for i in range(Hours):
    UsedTeachers = 0
    LockedTeachers = [0 for f in range(TotalTeachers)]
    for j in range(TotalJobs):
        if JobStatus[j] > 0:
            if UsedTeachers == TotalTeachers:
                break
            else:
                UsedTeachers += 1
                write_teacher(i, j)


print(Hours)
for i in Jobs:
    print(" ".join(map(str, i)))
