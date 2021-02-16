#!/bin/pypy3
n_ppl = int(input())
journal = {}

for i in range(n_ppl):
    f_name, l_name, mark1, mark2, mark3 = input().split()
    name = f_name + " " + l_name
    del f_name, l_name
    mark1, mark2, mark3 = int(mark1), int(mark2), int(mark3)
    journal[name] = (int((mark1 + mark2 + mark3) / 3), mark1, mark2, mark3)

print()
