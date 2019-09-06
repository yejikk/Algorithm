import sys
sys.stdin = open('토마토2.txt')

def wall(tz, tx, ty):
    if tz < 0 or tz >= H:
        return False
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= M:
        return False
    if arr[tz][tx][ty] == 1 or arr[tz][tx][ty] == -1:
        return False
    return True

def bfs():
    global cnt, tomato
    dz = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]

    while tomato:
        t = len(tomato)
        cnt += 1
        for i in range(t):
            z, x, y = tomato.pop(0)

            for j in range(6):
                tz = z + dz[j]
                tx = x + dx[j]
                ty = y + dy[j]
                if wall(tz, tx, ty):
                    arr[tz][tx][ty] = 1
                    tomato.append([tz, tx, ty])

M, N, H = map(int, input().split())
arr = [[[0]* M for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        arr[i][j] = list(map(int, input().split()))

flag = 1
tomato = []
for x in range(H):
    for y in range(N):
        for z in range(M):
            if arr[x][y][z] == 1:
                tomato.append([x, y, z])
            elif arr[x][y][z] == 0:
                flag = 0

if flag:
    print(0)

else:
    cnt = 0
    bfs()
    flag = 0
    for i in range(H):
        for j in range(N):
            if arr[i][j].count(0):
                flag = 1
                print(-1)
                break
        if flag:
            break

    if not flag:
        print(cnt-1)