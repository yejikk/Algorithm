import sys
sys.stdin = open('NQUEEN.txt')

def queen(x, y):
    for n in range(8):
        i, j = x, y
        while 0 <= i < N and 0 <= j < N:
            if arr[i][j] == 1:
                return False
            i = i + dx[n]
            j = j + dy[n]

    return True

def dfs(no):
    global cnt

    if no >= N:
        cnt += 1
        return

    for i in range(N):
        if queen(no, i):
            arr[no][i] = 1
            dfs(no+1)
            arr[no][i] = 0


N = int(input())
arr = [[0]*N for _ in range(N)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

cnt = 0

for i in range(N):
    arr[0][i] = 1
    dfs(1)
    arr[0][i] = 0

print(cnt)