import sys
sys.stdin = open('단지번호붙이기.txt')

def wall(tx, ty, cnt):
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= N:
        return False
    if arr[tx][ty] == 0 or arr[tx][ty] == cnt:
        return False

    return True

def dfs(x, y, cnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []
    stack.append([x, y])

    while stack:
        x, y = stack.pop()
        arr[x][y] = cnt
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty, cnt):
                if arr[tx][ty] == 1:
                    stack.append([tx, ty])

    num = count(cnt)
    return num

def count(cnt):
    num = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == cnt:
                num += 1
    return num


N = int(input())
arr = [[0]*N for _ in range(N)]

for n in range(N):
    arr[n] = list(map(int, input()))

cnt = 1
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            x = i
            y = j
            result.append(dfs(x, y, cnt))

result.sort()
print(len(result))
for j in range(len(result)):
    print(result[j])