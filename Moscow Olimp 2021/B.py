#!/bin/python3
a, b, c = [int(i) for i in input().split()]

if (a + b + c) % 3 != 0:
    print('IMPOSSIBLE')
else:
    m = (a + b + c) // 3
    array = [a, b, c]
    array.sort()
    if array[1] <= m:
        print(array[2] - m)
    else:
        print(array[2] - m + array[1] - m)
