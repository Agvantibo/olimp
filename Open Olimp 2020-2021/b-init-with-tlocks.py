#!/bin/python3
from math import ceil

TotalJobs, TotalTeachers, Passes = [int(i) for i in input().split()]

Teachers = [i + 1 for i in range(TotalTeachers)]
JobStatus = [Passes for i in range(TotalJobs)]
Hours = ceil(Passes * TotalJobs / TotalTeachers)
Jobs = [[0 for j in range(TotalJobs)] for i in range(Hours)]
# LockedTeachers = []


def release_lock():
    for i in range(TotalTeachers):
        LockedTeachers[i] = 0


def check_col_tem(row, col, teacher_index):
    res = True
    for i in range(row):
        if Jobs[i][col] == Teachers[teacher_index]:
            res = False
            break
    return res


def get_teach_index (row, col):

    odd_even = row % 2
    iter_miter = 0

    # if row > 0:
    #     row -= 1

    for t in range(TotalTeachers):
        if odd_even == 0:
            iter_miter = t
        else:
            iter_miter = TotalTeachers - t - 1

        if LockedTeachers [iter_miter] == 0:
            if check_col_tem(row, col, iter_miter):
                LockedTeachers[iter_miter] = 1
                return iter_miter


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
    release_lock()
    for j in range(TotalJobs):
        if JobStatus[j] > 0:
            if UsedTeachers == TotalTeachers:
                break
            else:
                UsedTeachers += 1
                Jobs[i][j] = Teachers[get_teach_index(i, j)]
                JobStatus[j] -= 1


print(Hours)
for i in Jobs:
    print(" ".join(map(str, i)))
