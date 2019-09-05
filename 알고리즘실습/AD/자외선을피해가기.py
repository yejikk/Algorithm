import sys
sys.stdin = open('자외선을피해가기.txt')

def BFS(r, c):
    que = []
    que.append([0, 0])
    rec[0][0] = arr[0][0]
    while que:
        r, c = que.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= 0 and nr < N and nc >= 0 and nc < N:
                if rec[nr][nc] > rec[r][c] + arr[nr][nc]:
                    rec[nr][nc] = rec[r][c] + arr[nr][nc]
                    que.append([nr, nc])
    return rec[N-1][N-1]

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
rec = [[10000000]*N for _ in range(N)]

sol = 1000000000000
rec[0][0] = arr[0][0]

print(BFS(0, 0))
