import sys
sys.stdin = open('동철이의프로그래밍대회.txt')

test = int(input())

for tc in range(1, test+1):
    N, M = map(int, input().split())
    person = 0
    score = 0
    result = []
    for i in range(N):
        score = 0
        problem = list(map(int, input().split()))
        for p in problem:
            if p == 1:
                score += 1
        result.append(score)

    for sc in result:
        if sc >= score:
            score = sc

    for ans in result:
        if sc == ans:
            person += 1

    print('#{} {} {}'.format(tc, person, score))