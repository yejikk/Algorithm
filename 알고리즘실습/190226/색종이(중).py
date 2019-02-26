import sys
sys.stdin = open('색종이(중).txt')

arr = [[0]*101 for _ in range(101)]
N = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for n in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
cnt = 0

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            for k in range(4):
                tx = i + dx[k]
                ty = j + dy[k]
                if arr[tx][ty] == 0:
                    cnt += 1
print(cnt)
for i in range(101):
    print(arr[i])