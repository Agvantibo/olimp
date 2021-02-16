#!/bin/pypy3


def replaced(array, ind1, ind2):  # Can't make a method out of it :(
    buffer = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = buffer

    return array


def inserted(array, array_length, element, index):
    output = []
    index -= 1
    for i in range(array_length + 1):  # A crutch. I am deeply ashamed of myself
        if i < index:
            output.append(array[i])
        elif i == index:
            output.append(element)
        else:
            output.append(array[i - 1])
    # return list(array[:index].append(element)) + array[:index + 1]  # The fuck it's not working?
    return output


array_l = int(input())
r = [int(i) for i in input().split()]
el, ind = [int(i) for i in input().split()]

print(" ".join(map(str, inserted(r, array_l, el, ind))))
