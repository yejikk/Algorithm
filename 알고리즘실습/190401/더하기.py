import sys
sys.stdin = open('더하기.txt')

def score(n, k, nsum):
    global cnt, flag
    if nsum > cnt:
        return

    if n == k:
        if nsum == K:
            flag = 1
            cnt = nsum
        return
    else:
        temp[k] = 1
        score(n, k+1, nsum + num[k])
        temp[k] = 0
        score(n, k+1, nsum)


test = int(input())

for tc in range(test):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    temp = [0] * N
    flag = 0
    cnt = 10000000
    score(N, 0, 0)
    if flag:
        print('YES')
    else:
        print('NO')