import sys
sys.stdin = open('최소합.txt')

def minsum(x, y, nsum):
    global nmin
    if nsum > nmin:
        return

    if x == endx and y == endy:
        if nsum < nmin:
            nmin = nsum
        return

    for i in range(2):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx <= N-1 and ty <= N-1:
            minsum(tx, ty, nsum + arr[tx][ty])

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for k in range(N):
        arr[k] = list(map(int, input().split()))

    dx = [0, 1]
    dy = [1, 0]
    endx = N-1
    endy = N-1
    nmin = 999999999

    minsum(0, 0, arr[0][0])
    print('#{} {}'.format(tc, nmin))