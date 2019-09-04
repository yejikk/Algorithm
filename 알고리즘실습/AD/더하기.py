import sys
sys.stdin = open('더하기.txt')

def dfs(no, cnt):
    global K, flag
    if cnt > K:
        return

    if cnt == K:
        flag = 1
        return

    if no >= N:
        if cnt == K:
            flag = 1

        return

    temp[no] = num[no]
    dfs(no+1, cnt+temp[no])
    temp[no] = 0
    dfs(no+1, cnt)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    temp = [0] * N

    flag = 0
    dfs(0, 0)

    if flag:
        print('YES')
    else:
        print('NO')