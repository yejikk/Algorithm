import sys
sys.stdin = open('전자카트.txt')

def dfs(n, nsum):
    global nmin
    if nsum > nmin:
        return

    if n >= N:
        if nsum < nmin:
            nmin = nsum
        return

    for i in range(N):
        if chk[i] == 1:
            continue
        if arr[n][i]:
            chk[i] = 1
            dfs(n+1, nsum + arr[n][i])
            chk[i] = 0

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    chk = [0] * (N+1)
    nmin = 10000000
    dfs(0, 0)
    print('#{} {}'.format(tc, nmin))