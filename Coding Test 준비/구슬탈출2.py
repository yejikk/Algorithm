import sys
sys.stdin = open('구슬탈출2.txt')

def move(x, y, dx, dy, di):
    while ball[x][y] != '#' and ball[x][y] != 'O':
        x += dx
        y += dy
        di += 1

    return x, y, di

def bfs():
    global chk, dx, dy
    while q:
        rx, ry, bx, by, di = q.pop(0)
        if di >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if ball[nrx][nry] == 'O':
                print(di+1)
                return
            if ball[nbx][nby] == 'O':
                continue
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]




N, M = map(int, input().split())

# R공, B공을 동시에 돌려야함
# 동시에 돌려야 하기 때문에 4차원 배열 사용
chk = [[[[0]*M for _ in range(N)]for _ in range(M)]for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ball = [[0]*M for _ in range(N)]
for n in range(N):
    ball[n] = list(map(str, input()))
    print(ball[n])

rx, ry, bx, by = 0
q = []
for i in range(N):
    for j in range(M):
        if ball[i][j] == 'R':
            rx, ry = i, j
        elif ball[i][j] == 'B':
            bx, by = i, j

q.append([rx, ry, bx, by, 0])
chk[rx][ry][bx][by] = 1