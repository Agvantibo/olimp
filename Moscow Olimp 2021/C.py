#!/bin/pypy3
from sys import exit

tests = int(input())
test_scores = [int(i) for i in input().split()]
final_score = int(input())
n_submissions = int(input())

submissions = [[int(i) for i in input().split()] for i in range(n_submissions)]

penalty = 0
MaxScore = 0
for i in range(n_submissions):
    FullTests = True
    score = 0
    for j in range(tests):
        if submissions[i][j] == 1:
            score += test_scores[j]
        elif submissions[i][j] == 0:
            FullTests = False
        else:
            exit("Press F to pay respects")
    score -= penalty
    if FullTests:
        score += final_score
    if score > MaxScore:
        MaxScore = score
    print(MaxScore)
    penalty += 2
