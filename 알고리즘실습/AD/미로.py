import sys
sys.stdin = open('미로.txt')

def wall(tx, ty):
    if tx < 0 or tx >= N:
        return False
    if ty < 0 or ty >= N:
        return False
    if arr[tx][ty] == 1 or arr[tx][ty] == 9:
        return False

    return True

def dfs(x, y):
    flag = 0
    stack = []
    stack.append([x, y])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        temp = stack.pop()
        x = temp[0]
        y = temp[1]
        arr[x][y] = 9
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty):
                if arr[tx][ty] == 3:
                    flag = 1
                    return 1
                    break
                elif arr[tx][ty] == 0:
                    stack.append([tx, ty])

        if flag:
            break

    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    for n in range(N):
        arr[n] = list(map(int, input()))

    flag = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                flag = 1
                x = i
                y = j
                break
        if flag:
            break

    result = dfs(x, y)
    print('#{} {}'.format(tc, result))