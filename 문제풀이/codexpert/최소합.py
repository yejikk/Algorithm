import sys
sys.stdin = open('최소합.txt')

def DFS(x, y, nsum):
    global nmin
    if nsum > nmin:
        return

    if x == N-1 and y == N-1:
        if nsum < nmin:
            nmin = nsum
        return

    for i in range(2):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= N or ty < 0 or ty >= N:
            continue
        DFS(tx, ty, nsum + arr[tx][ty])

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    dx = [1, 0]
    dy = [0, 1]
    nmin = 10000000
    DFS(0, 0, arr[0][0])
    print('#{} {}'.format(tc, nmin))