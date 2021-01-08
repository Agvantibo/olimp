#!/bin/python3
from math import ceil

n, m, k = [int(i) for i in input().split()]
# n - jobs, m - tutors, k - passes

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
            status.pop(cur_index)
            if used_teachers == t_limit:
                return indices


for i in range(Hours):
    tc += 1
    priorities = compose_priority(JobStatus, n, m)
    for j in priorities:
        if JobStatus[j] != 0:
            tc += 1
            JobStatus[j] -= 1
            Jobs[i][j] = get_teacher(tc, m)

print(Hours)
for i in Jobs:
    print(" ".join(map(str, i)))
