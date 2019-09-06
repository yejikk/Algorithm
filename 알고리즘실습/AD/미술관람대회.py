import sys
sys.stdin = open('미술관람대회.txt')

def wall(tx, ty, test):
    if tx < 0 or tx >= N:
        return False
    elif ty < 0 or ty >= N:
        return False
    elif test == 'test1':
        if v1[tx][ty] != 0:
            return False
    elif test == 'test2':
        if v2[tx][ty] != 0:
            return False
    return True

def bfs1(x, y):
    global dx, dy, num1
    q1 = []
    q1.append([x, y])
    color1 = arr[x][y]
    while q1:
        x, y = q1.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty, 'test1'):
                if arr[tx][ty] == color1:
                    v1[tx][ty] = num1
                    q1.append([tx, ty])

def bfs2(x, y):
    global dx, dy, num2
    q2 = []
    q2.append([x, y])
    color2 = arr[x][y]
    while q2:
        x, y = q2.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if wall(tx, ty, 'test2'):
                if color2 == 'R' or color2 == 'G':
                    if arr[tx][ty] == 'R' or arr[tx][ty] == 'G':
                        v2[tx][ty] = num1
                        q2.append([tx, ty])
                elif color2 == 'B':
                    if arr[tx][ty] == 'B':
                        v2[tx][ty] = num1
                        q2.append([tx, ty])

# 두가지 경우 -> visited
N = int(input())
arr = [[0]*N for _ in range(N)]

for i in range(N):
    arr[i] = list(map(str, input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

v1 = [[0]*N for _ in range(N)]
v2 = [[0]*N for _ in range(N)]

num1 = 0
num2 = 0
for i in range(N):
    for j in range(N):
        if v1[i][j] == 0:
            num1 += 1
            v1[i][j] == num1
            bfs1(i, j)

        if v2[i][j] == 0:
            num2 += 1
            v2[i][j] = num2
            bfs2(i, j)

print(num1, num2)
