import sys
sys.stdin = open('달팽이사각형.txt')

def wall(tx, ty, n):
    if (tx < 0 or tx >= n) or (ty < 0 or ty >= n):
        return False
    if arr[tx][ty] != 0:
        return False
    return True

N = int(input())
arr = [[0]*N for _ in range(N)]

x = 0
y = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
arr[0][0] = 1
num = arr[0][0] + 1

while num <= N*N:
    if direction % 4 == 0:
        x = dx[0] + x
        y = dy[0] + y
        if wall(x, y, N):
            arr[x][y] = num
            num += 1
        else:
            direction += 1
            y = y - 1

    elif direction % 4 == 1:
        x = dx[1] + x
        y = dy[1] + y
        if wall(x, y, N):
            arr[x][y] = num
            num += 1
        else:
            direction += 1
            x = x - 1

    elif direction % 4 == 2:
        x = dx[2] + x
        y = dy[2] + y
        if wall(x, y, N):
            arr[x][y] = num
            num += 1
        else:
            direction += 1
            y = y + 1

    elif direction % 4 == 3:
        x = dx[3] + x
        y = dy[3] + y
        if wall(x, y, N):
            arr[x][y] = num
            num += 1
        else:
            direction += 1
            x = x + 1

for i in range(N):
    print(' '.join(map(str, arr[i])))