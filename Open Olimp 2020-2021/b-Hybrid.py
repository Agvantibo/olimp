#!/bin/python3
from math import ceil

# BUGGY TESTS: 9 6 3

TotalJobs, TotalTeachers, Passes = [int(i) for i in input().split()]
if TotalJobs == 0 or Passes == 0:
    print(0)
else:
    Hours = ceil(Passes * TotalJobs / TotalTeachers)
    Jobs = [[0 for j in range(TotalJobs)] for i in range(Hours)]
    UsedTeachers = 0

    if TotalJobs % TotalTeachers == 0 or TotalJobs % Passes == 0:

        def get_teacher(cur, length):
            return Teachers[cur % length]
        
        JobStatus = [Passes for i in range(TotalJobs)]
        TeacherCounter = -2
        Teachers = [i + 1 for i in range(TotalTeachers)]

        for i in range(Hours):
            TeacherCounter += 1
            UsedTeachers = 0
            for j in range(TotalJobs):
                if JobStatus[j] != 0:
                    TeacherCounter += 1
                    UsedTeachers += 1
                    JobStatus[j] -= 1
                    Jobs[i][j] = get_teacher(TeacherCounter, TotalTeachers)
                    if UsedTeachers == TotalTeachers:
                        break

    else:

        def check_job(row, column, value):
            # if JobStatus[column] > 0 and value != 0:
            if value != 0:
                # JobStatus[column] -= 1
                Jobs[row][column] = value
                return 0
            else:
                return 1


        for i in range(TotalJobs):
            UsedTeachers += 1
            check_job(0, i, i + 1)
            if UsedTeachers == TotalTeachers:
                break

        for i in range(1, Hours):
            for j in range(TotalJobs - 1):
                check_job(i, j, Jobs[i - 1][j + 1])
            check_job(i, -1, Jobs[i - 1][0])

    print(Hours)
    for i in Jobs:
        print(" ".join(map(str, i)))
