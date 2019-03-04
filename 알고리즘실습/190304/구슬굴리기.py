import sys
sys.stdin = open('구슬굴리기.txt')

def wall(x, y, N, M):
    if x < 0 or x >= N:
        return False
    if y < 0 or y >= M:
        return False
    if arr[x][y] == 1:
        return False
    return True

def direction(num, x, y):
    if num == 1:
        x -= 1
    elif num == 2:
        x += 1
    elif num == 3:
        y -= 1
    elif num == 4:
        y += 1
    return x, y

N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

dnum = int(input())
dirc = list(map(int, input().split()))

flag = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            flag = 1
            x = i
            y = j
            break
    if flag:
        break
n = 0
cnt = 1
while True:
    tx, ty = direction(dirc[n], x, y)
    if wall(tx, ty, N, M):
        if arr[tx][ty] == 0:
            cnt += 1
            arr[tx][ty] = 9
        elif arr[tx][ty] == 9:
            cnt += 0
        x = tx
        y = ty
    else:
        n += 1

    if n == dnum:
        break

print(cnt)