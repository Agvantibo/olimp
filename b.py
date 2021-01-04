#!/bin/python3
from math import ceil

TotalJobs, TotalTeachers, Passes = [int(i) for i in input().split()]

Teachers = [i + 1 for i in range(TotalTeachers)]
JobStatus = [Passes for i in range(TotalJobs)]
Hours = ceil(Passes * TotalJobs / TotalTeachers)
Jobs = [[0 for j in range(TotalJobs)] for i in range(Hours)]
#LockedTeachers = []

def releaseLock():
    for i in range (TotalTeachers):
        LockedTeachers[i] = 0

def getTeachIndex (row, col):

    chetNechet = row % 2
    iterMiter = 0

    if row > 0:
        row -= 1

    for t in range (TotalTeachers):
        if chetNechet == 0:
            iterMiter = t
        else:
            iterMiter = TotalTeachers - t -1

        if LockedTeachers [iterMiter] == 0:
            if Jobs[row][col] != Teachers[iterMiter]:
                LockedTeachers[iterMiter] = 1
                return iterMiter

def write_teacher(i1, i2):
    for a in range(TotalTeachers):
        if LockedTeachers[a] == 0:
            if i1 == 0:
                LockedTeachers[a] = 1
                Jobs[i1][i2] = Teachers[a]
            elif Teachers[a] == Jobs[i1-1][i2]:
                continue
            else:
                LockedTeachers[a] = 1
                Jobs[i1][i2] = Teachers[a]

LockedTeachers = [0 for f in range(TotalTeachers)]
for i in range(Hours):
    UsedTeachers = 0
    releaseLock()
    for j in range(TotalJobs):
        if JobStatus[j] > 0:
            if UsedTeachers == TotalTeachers:
                break
            else:
                UsedTeachers += 1
                Jobs[i][j] = Teachers[getTeachIndex(i, j)]
                JobStatus[j] -= 1


print(Hours)
for i in Jobs:
    print(" ".join(map(str, i)))
