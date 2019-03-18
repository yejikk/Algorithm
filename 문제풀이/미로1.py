import sys
sys.stdin = open('미로1.txt')

def wall(tx, ty):
    if tx < 0 or tx >= 16:
        return False
    if ty < 0 or ty >= 16:
        return False
    if arr[tx][ty] == 1:
        return False
    return True

def bfs(x, y):
    global visited, arr
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = []
    queue.append([x, y])
    flag = 0
    while len(queue) != 0:
        v = queue.pop(0)
        x = v[0]
        y = v[1]
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty) and [tx, ty] not in visited:
                if arr[tx][ty] == 3:
                    flag = 1
                    return 1
                    break
                else:
                    queue.append([tx, ty])
                    visited.append([tx, ty])
        if flag:
            break
    return 0

for tc in range(1, 11):
    T = int(input())
    arr = [[0]*16 for _ in range(16)]
    visited = []
    for k in range(16):
        arr[k] = list(map(int, input()))

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                x = i
                y = j

    result = bfs(x, y)
    print('#{} {}'.format(tc, result))