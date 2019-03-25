import sys
sys.stdin = open('저글링.txt')

def wall(tx, ty):
    global N, M, arr
    if tx < 0 or tx >= M:
        return False
    if ty < 0 or ty >= N:
        return False
    if arr[ty][tx] == 0:
        return False
    return True

def BFS(x, y):
    global arr
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = []
    queue.append([x, y])
    arr[y][x] = 3
    cnt = 3
    while queue:
        v = queue.pop(0)
        x = v[0]
        y = v[1]
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty):
                if arr[ty][tx] == 1:
                    queue.append([tx, ty])
                    arr[ty][tx] = arr[y][x] + 1

    return arr

M, N = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for k in range(N):
    arr[k] = list(map(int, input()))

startx, starty = map(int, input().split())
startx -= 1
starty -= 1

BFS(startx, starty)
# print(arr)

time = 0
nodie = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            nodie += 1
        if arr[i][j] > time:
            time = arr[i][j]
print(time)
print(nodie)


