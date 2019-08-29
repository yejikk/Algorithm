import sys
sys.stdin = open('최소비용.txt')

def BFS():
    queue = []
    queue.append([0, 0])
    rec[0][0] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue
            if rec[tx][ty] > rec[x][y] + arr[tx][ty]:
                queue.append([tx, ty])
                rec[tx][ty] = rec[x][y] + arr[tx][ty]

    return rec[N-1][N-1]

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    rec = [[0] * N for _ in range(N)]
    nmin = 10000000
    BFS()
    print(nmin)
    print(BFS())