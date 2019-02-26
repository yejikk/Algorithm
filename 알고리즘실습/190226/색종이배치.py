import sys
sys.stdin = open('색종이배치.txt')

arr = [[0]*100 for _ in range(100)]

cnt = 0
type3 = 0
flag = 1

x1, y1, dx1, dy1 = list(map(int, input().split()))
x2, y2, dx2, dy2 = list(map(int, input().split()))

for i in range(x1, x1+dx1):
    for j in range(y1, y1+dy1):
        arr[i][j] = 1

for i in range(x1-1, x1+dx1+1):
    arr[i][y1-1] = 2
for i in range(y1-1, y1+dx1+1):
    arr[x1-1][i] = 2
for i in range(y1+dy1, y1-1, -1):
    arr[x1+dx1][i] = 2
for i in range(x1+dx1, x1-1, -1):
    arr[i][dy1+y1] = 2

for i in range(x2, x2+dx2):
    for j in range(y2, y2+dy2):
        arr[i][j] += 1

for i in range(x2, x2+dx2):
    for j in range(y2, y2+dy2):
        if arr[i][j] == 2:
            type3 += 1

        elif arr[i][j] == 3:
            cnt += 1

if cnt == 1:
    print(1)
elif type3 >= 1:
    print(3)
elif type3 == 0 and cnt > 1:
    print(2)
elif cnt == 0:
    print(4)

for i in range(100):
    print(arr[i])

