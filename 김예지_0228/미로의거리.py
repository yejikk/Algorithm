import sys
sys.stdin = open('미로의거리.txt')

def wall(tx, ty, n):
    if tx < 0 or tx >= n:
        return False
    if ty < 0 or ty >= n:
        return False
    if arr[tx][ty] == 9:
        return False
    elif arr[tx][ty] == 1:
        return False
    return True

def distance(x, y, n):
    global arr

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    flag = 0
    queue = []
    cnt = 0
    queue.append([x, y])
    while queue:
        exit = []
        wallcnt = 0
        v = queue.pop(0)
        arr[v[0]][v[1]] = 9
        i = v[0]
        j = v[1]
        for k in range(4):
            tx = i + dx[k]
            ty = j + dy[k]
            if wall(tx, ty, n):
                if arr[tx][ty] == 3:
                    flag = 1
                    return cnt
                    break
                else:
                    cnt += 1
                    queue.append([tx, ty])
                    arr[tx][ty] = 9
            else:
                wallcnt += 1

        if flag:
            break
        else:
            if wallcnt >= 4:
                cnt -= wallcnt
    return 0

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    flag = 0

    for i in range(N):
        arr[i] = list(map(int, input()))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = i
                y = j
                flag = 1
                break
        if flag:
            break

    result = distance(x, y, N)

    print(f'#{tc} {result}')