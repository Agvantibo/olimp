#!/bin/pypy3


def replaced(array, ind1, ind2):  # Can't make a method out of it :(
    buffer = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = buffer

    return array


int(input()) # skippin' the element number
r = [int(i) for i in input().split()]
isSorted = False

r.sort()

print(" ".join(map(str, r)))
