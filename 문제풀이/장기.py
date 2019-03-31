import sys, pprint
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
    flag = 0
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = []
    queue.append([x, y, 1])
    while queue:
        v = queue.pop(0)
        x = v[0]
        y = v[1]
        cnt = v[2]
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty):
                if arr[tx][ty] == 3:
                    flag = 1
                    return cnt
                    break
                else:
                    queue.append([tx, ty, cnt+1])
                    arr[tx][ty] = 99
        if flag:
            break


N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
arr[sx][sy] = 2
ex -= 1
ey -= 1
arr[ex][ey] = 3

result = bfs(sx, sy)
print(result)