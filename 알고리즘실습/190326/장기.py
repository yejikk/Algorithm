import sys
sys.stdin = open('장기.txt')

def wall(tx, ty):
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= M:
        return False
    if arr[tx][ty] == 99:
        return False
    return True

def bfs(x, y):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [-1, 1, -1, 1, -2, 2, -2, 2]
    queue = []
    queue.append([x, y, 1])
    arr[x][y] = 99
    while queue:
        v = queue.pop(0)
        x = v[0]
        y = v[1]
        cnt = v[2]
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty):
                if tx == ex and ty == ey:
                    return cnt
                    break
                else:
                    queue.append([tx, ty, cnt+1])
                    arr[tx][ty] = 99

    return -1

N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1
result = bfs(sx, sy)
print(result)

