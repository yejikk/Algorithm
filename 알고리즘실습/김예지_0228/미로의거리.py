import sys
sys.stdin = open('미로의거리.txt')
'''
BFS 차수를 이용해서 문제풀기!
visited check를 이용하기 [x][y]가능
'''
def wall(tx, ty, n):
    if tx < 0 or tx >= n:
        return False
    if ty < 0 or ty >= n:
        return False
    if arr[tx][ty] == 1:
        return False
    return True

def distance(x, y, n):
    global arr, visited
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = []
    flag = 0
    queue.append([x, y])
    visited[x][y] = 1
    while len(queue) != 0:
        t = queue.pop(0)
        x = t[0]
        y = t[1]
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty, n):
                if arr[tx][ty] == 3:
                    flag = 1
                    return visited[x][y] - 1
                    break
                elif arr[tx][ty] == 0 and visited[tx][ty] == 0:
                    queue.append([tx, ty])
                    visited[tx][ty] = visited[x][y] + 1
        if flag:
            break
    return 0

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
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