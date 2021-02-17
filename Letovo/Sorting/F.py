#!/bin/pypy3


def replaced(array, ind1, ind2):  # Can't make a method out of it :(
    buffer = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = buffer

    return array


n_ppl = int(input())
marks = []
ppl = []

for i in range(n_ppl):
    f_name, l_name, mark1, mark2, mark3 = input().split()
    name = f_name + " " + l_name
    del f_name, l_name
    mark1, mark2, mark3 = int(mark1), int(mark2), int(mark3)
    marks.append(int((mark1 + mark2 + mark3) / 3))
    ppl.append(name)
del mark1, mark2, mark3, name

for i in range(2):
    coolest = marks.index(max(marks))
    print(ppl[coolest])
    ppl.pop(coolest)
    marks.pop(coolest)

while True:
    coolest = marks.index(max(marks))
    print(ppl[coolest])
    ppl.pop(coolest)
    marks.pop(coolest)
    if not ppl:
        break
    next_coolest = marks.index(max(marks))
    if marks[next_coolest] != marks[coolest]:
        break
