import sys
sys.stdin = open('미로.txt')

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

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input()))

    flag = 0
    stack = []
    visited = []
    dx = [-1, 1, 0, 0] # 위, 아래 이동
    dy = [0, 0, -1, 1] # 왼쪽, 오른쪽 이동

    startx, starty = start(N, arr) # 출발지 찾기

    stack.append([startx, starty])
    # print(maze)
    while len(stack) != 0:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            x = v[0]
            y = v[1]
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if wall(tx, ty, N):
                    if arr[tx][ty] == 3: # 이동한 곳이 3인지 검사
                        flag = 1
                        break
                if wall(tx, ty, N):
                    if arr[tx][ty] == 0:
                        stack.append([tx, ty])

        if flag: # 도착했을 경우 1을 출력
            print(f'#{tc} 1')
            break

    if not flag: # 도착하지 못했을 경우 0을 출력
        print(f'#{tc} 0')