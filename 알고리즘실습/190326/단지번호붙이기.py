import sys
sys.stdin = open('단지번호붙이기.txt')

def wall(tx, ty):
    global N, arr
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= N:
        return False
    if arr[tx][ty] == 0:
        return False
    return True

def dfs(x, y):
    global arr
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []
    cnt = 0
    stack.append([x, y])
    while stack:
        v = stack.pop()
        x = v[0]
        y = v[1]
        if arr[x][y] == 1:
            arr[x][y] = 0
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if wall(tx, ty):
                    stack.append([tx, ty])
            cnt += 1
    return cnt

N = int(input())
arr = [[0]*N for _ in range(N)]
for k in range(N):
    arr[k] = list(map(int, input()))

cnt = 0
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            x = i
            y = j
            cnt += 1
            find = dfs(x, y)
            home.append(find)

print(cnt)
home.sort()
if cnt != 0:
    for n in range(cnt):
        print(home[n])