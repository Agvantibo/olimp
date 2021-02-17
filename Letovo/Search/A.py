#!/bin/pypy3


def binary_search_num(seq, query, seq_sorted=False, seq_length=-1, seq_start=0, seq_stop=None):
    index = -1

    if not seq_sorted:
        seq.sort()
    if seq_length == -1:
        seq_length = len(seq)
    if seq_stop is None:
        seq_stop = seq_length - 1

    not_found = True
    while not_found:
        seq_middle_index = (seq_stop - seq_start) // 2
        if query == seq[seq_start:seq_stop][seq_middle_index]:
            return seq_middle_index
    return "-1"


l_data, l_queries = [int(i) for i in input().split()]
data = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()]

for i in queries:
    if i in data:
        print("YES")
    else:
        print("NO")
