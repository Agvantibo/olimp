#!/bin/python3
from math import ceil

n, m, k = [int(i) for i in input().split()]
# n - jobs, m - tutors, k - passes

# BUGGY TESTS: 9 3 3;

Teachers = [i + 1 for i in range(m)]
JobStatus = [k for i in range(n)]
Hours = ceil(k * n / m)
Jobs = [[0 for j in range(n)] for i in range(Hours)]
tc = -2


def get_teacher(cur, length):
    return Teachers[cur % length]


def compose_priority(status_origin, len_status, t_limit):
    status = status_origin.copy()
    indices = []
    used_teachers = 0
    for i in range(len_status):
        used_teachers += 1
        cur_max = max(status)
        if cur_max in status:
            cur_index = status.index(cur_max)
            indices.append(cur_index)
            status[cur_index] = -1  # Lock the already-reported targets
            # it's -1 because -1 couldn't possibly occur naturally in JobStatus.
            if used_teachers == t_limit:
                return indices


def check_originality(current_string, current_char, current_index):
    for f in range(current_string):
        if Jobs[f][current_index] == current_char:
            return False
    for f in range(n):
        if Jobs[current_string][f] == current_char and f != current_index:
            return False
    return True

FlipFlop = False

for i in range(Hours):
    if FlipFlop:
        FlipFlop = False
    else:
        FlipFlop = True
        tc += 1
    tc += m
    priorities = compose_priority(JobStatus, n, m)
    for j in priorities:
        if JobStatus[j] != 0:
            JobStatus[j] -= 1
            ConfirmedTeacher = 'F'
            for w in range(m):
                tc += 1
                TeacherTry = get_teacher(tc, m)
                if check_originality(i, TeacherTry, j):
                    ConfirmedTeacher = TeacherTry
            Jobs[i][j] = ConfirmedTeacher

print(Hours)
for i in Jobs:
    print(" ".join(map(str, i)))
