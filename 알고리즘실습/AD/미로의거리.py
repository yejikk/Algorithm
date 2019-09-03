import sys
sys.stdin = open('미로의거리.txt')

def wall(tx, ty):
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= N:
        return False
    if maze[tx][ty] == 1 or maze[tx][ty] == 9:
        return False

    return True

def bfs(x, y):
    queue = []
    queue.append([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    flag = 0

    while queue:
        v = queue.pop(0)
        x = v[0]
        y = v[1]
        maze[x][y] = 9

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty):
                if maze[tx][ty] == 3:
                    flag = 1
                    return visited[x][y]
                    break
                if maze[tx][ty] == 0 and visited[tx][ty] == 0:
                    queue.append([tx, ty])
                    visited[tx][ty] = visited[x][y] + 1

        if flag:
            break
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for n in range(N):
        maze[n] = list(map(int, input()))

    flag = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x = i
                y = j
                flag = 1
                break
        if flag:
            break

    result = bfs(x, y)
    print('#{} {}'.format(tc, result))