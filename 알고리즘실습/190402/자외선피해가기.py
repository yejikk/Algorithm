import sys
sys.stdin = open('자외선피해가기.txt')

def BFS():
    queue = []
    queue.append([0, 0])
    rec[0][0] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue
            if rec[tx][ty] > rec[x][y] + arr[tx][ty]:
                queue.append([tx, ty])
                rec[tx][ty] = rec[x][y] + arr[tx][ty]

    return rec[N-1][N-1]

def DFS(x, y, nsum):
    global nmin
    if nsum > nmin:
        return

    if x == N-1 and y == N-1:
        if nsum < nmin:
            nmin = nsum
        return

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx <= N-1 and 0 <= ty <= N-1:
            DFS(tx, ty, nsum + arr[tx][ty])

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

rec = [[0]*N for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
nmin = 10000000
DFS(0, 0, arr[0][0])
print(nmin)
print(BFS())
print(rec)