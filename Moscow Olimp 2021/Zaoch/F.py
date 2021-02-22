#!/bin/pypy3

Message = input()
n_hypothesis = int(input())
a_hypothesis = []
for i in range(n_hypothesis):
    a_hypothesis.append(input())

Message = sorted(Message)

for i in a_hypothesis:
    if sorted(i) == Message:
        print(i)
