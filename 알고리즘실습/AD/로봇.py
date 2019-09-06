import sys
sys.stdin = open('로봇')

def wall(tx, ty):
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= M:
        return False
    if arr[tx][ty] == 0:
        return False

    return True

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

sx, sy, di = map(int, input().split())
sx -= 1
sy -= 1

ex, ey, di = map(int, input().split())
ex -= 1
ey -= 1
