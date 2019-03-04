import sys
sys.stdin = open('사냥꾼.txt')

def mountain(arr, N):
    hunter = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                hunter.append([i, j])
    return hunter

def wall(x, y, N):
    if x < 0 or x >= N:
        return False
    if y < 0 or y >= N:
        return False
    if arr[x][y] == 1 or arr[x][y] == 0:
        return False
    return True

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

hunter = mountain(arr, N)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
cnt = 0
while True:
    if len(hunter) == 0:
        break
    else:
        ht = hunter.pop(0)
        x = ht[0]
        y = ht[1]
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty, N):
                if arr[tx][ty] == 9:
                    cnt += 0
                else:
                    cnt += 1
                    arr[tx][ty] = 9
                while True:
                    tx = tx + dx[i]
                    ty = ty + dy[i]
                    if wall(tx, ty, N):
                        if arr[tx][ty] == 9:
                            continue
                        else:
                            cnt += 1
                            arr[tx][ty] = 9
                    else:
                        break
print(cnt)