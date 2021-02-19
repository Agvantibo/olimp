#!/bin/pypy3


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


input()
data = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()]

for i in queries:
    if binary_search(data, 0, len(data) - 1, i) == -1:
        print("NO")
    else:
        print("YES")
