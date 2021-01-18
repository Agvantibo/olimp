#!/bin/python3
tests = int(input())
test_scores = []
for i in range(tests):
    test_scores.append(int(input()))
final_score = int(input())
n_submissions = int(input())

submissions = [[] for i in range(n_submissions)]
for i in submissions:
    for j in range(tests):
        if int(input()) == 1:
            i.append(True)
        else:
            i.append(False)

for i in range(n_submissions):
    score = 0
    penalty = i * 2
    for j in range(tests):
        if submissions[i][j]:
            score += test_scores[j]
    print(score-penalty)
