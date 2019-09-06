import sys
sys.stdin = open('토마토.txt')

def wall(tx, ty):
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= M:
        return False
    if arr[tx][ty] == 1 or arr[tx][ty] == -1:
        return False
    return True

def bfs():
    global tomato, cnt

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while tomato:
        cnt += 1
        for i in range(len(tomato)):
            x, y = tomato.pop(0)
            for j in range(4):
                tx = x + dx[j]
                ty = y + dy[j]
                if wall(tx, ty):
                    arr[tx][ty] = 1
                    tomato.append([tx, ty])


M, N = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for n in range(N):
    arr[n] = list(map(int, input().split()))

tomato = []
cnt = 0
flag = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            flag = 0
            tomato.append([i, j])

if flag:
    print(0)

else:
    bfs()
    for i in range(N):
        if arr[i].count(0):
            print(-1)
            break
        else:
            print(cnt-1)
            break
