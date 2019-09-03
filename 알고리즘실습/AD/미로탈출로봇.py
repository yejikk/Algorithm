import sys
sys.stdin = open('미로탈출로봇.txt')

def wall(tx, ty):
    if tx < 0 or tx >= Y:
        return False
    if ty < 0 or ty >= X:
        return False
    if arr[tx][ty] == 1 or arr[tx][ty] == 9:
        return False

    return True

def bfs():
    global sx, sy, ex, ey, visited

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = []
    queue.append([sx, sy])

    flag = 0

    while queue:
        v = queue.pop(0)
        x = v[1]
        y = v[0]
        arr[x][y] = 9
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty):
                if tx == ey and ty == ex:
                    flag = 1
                    return visited[x][y] + 1

                elif arr[tx][ty] == 0 and visited[tx][ty] == 0:
                    queue.append([ty, tx])
                    visited[tx][ty] = visited[x][y] + 1

        if flag:
            break

    return 0

X, Y = map(int, input().split())

sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1

arr = [[0]*X for _ in range(Y)]
visited = [[0]*X for _ in range(Y)]

for n in range(Y):
    arr[n] = list(map(int, input()))

result = bfs()
print(result)