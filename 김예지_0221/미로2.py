import sys
sys.stdin = open('미로2.txt')

def start(n, arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x = i
                y = j
    return x, y


def wall(tx, ty, n):
    if (tx >= 0 and tx < n) and (ty >= 0 and ty < n):
        return True

    return False

for tc in range(10):
    case = input()
    N = 100
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input()))

    flag = 0
    stack = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    startx, starty = start(N, arr)
    stack.append([startx, starty])

    while len(stack) != 0:
        v = stack.pop()
        arr[v[0]][v[1]] = 9
        x = v[0]
        y = v[1]
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty, N):
                if arr[tx][ty] == 3:
                    flag = 1
                    break
            if wall(tx, ty, N):
                if arr[tx][ty] == 0:
                    # arr[tx][ty] = 9
                    stack.append([tx, ty])

        if flag:
            print(f'#{case} 1')
            break

    if not flag:
        print(f'#{case} 0')