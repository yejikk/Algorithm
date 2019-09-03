import sys
sys.stdin = open('저글링방사능오염.txt')

def wall(tx, ty):
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= M:
        return False
    if arr[tx][ty] == 0:
        return False

    return True

def bfs(y, x):
    queue = []
    queue.append([x, y, 3])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, cnt = queue.pop(0)
        cnt += 1
        arr[x][y] = cnt
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty):
                if arr[tx][ty] == 1:
                    queue.append([tx, ty, cnt])

    alive = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                alive += 1

    return cnt-1, alive

M, N = map(int, input().split())

arr = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input()))

y, x = map(int, input().split())

y -= 1
x -= 1

result = bfs(y, x)
print(' '.join(map(str, result)))