import sys
sys.stdin = open('미로탈출.txt')

def wall(x, y, N):
    if x < 0 or x >= N:
        return False
    if y < 0 or y >= N:
        return False
    return True

def direction(num, x, y):
    if num == 1:
        x += 1
    elif num == 2:
        y -= 1
    elif num == 3:
        x -= 1
    elif num == 4:
        y += 1
    return x, y

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))
dirc = list(map(int, input().split()))

x = 0
y = 0
n = 0
cnt = 0

while True:
    i, j = direction(dirc[n%4], x, y)
    if wall(i, j, N):
        if arr[i][j] == 0:
            x = i
            y = j
            arr[i][j] = 9
            cnt += 1
        elif arr[i][j] == 9:
            break
        else:
            n += 1
    else:
        n += 1

print(cnt)