import sys, pprint
sys.stdin = open('색종이배치.txt')

def outside(arr):
    global x1, y1, dx1, dx2
    for i in range(x1 - 1, x1 + dx1 + 1):
        arr[i][y1 - 1] = 99
    for i in range(y1 - 1, y1 + dx1 + 1):
        arr[x1 - 1][i] = 99
    for i in range(y1 + dy1, y1 - 1, -1):
        arr[x1 + dx1][i] = 99
    for i in range(x1 + dx1, x1 - 1, -1):
        arr[i][dy1 + y1] = 99
    return arr

arr = [[0]*100 for _ in range(100)]

x1, y1, dx1, dy1 = map(int, input().split())
x2, y2, dx2, dy2 = map(int, input().split())

for i in range(x1, x1+dx1):
    for j in range(y1, y1+dy1):
        arr[i][j] += 1

arr = outside(arr)

for x in range(x2, x2+dx2):
    for y in range(y2, y2+dy2):
        arr[x][y] += 1

cnt1 = 0 # type1, type2 찾는 cnt1
cnt2 = 0 # type3 찾는 cnt2

for n in range(100):
    for m in range(100):
        if arr[n][m] == 100:
            cnt1 += 1
        if arr[n][m] == 2:
            cnt2 += 1

if cnt2 > 0:
    print(3)
elif cnt1 == 1:
    print(1)
elif cnt1 > 1:
    print(2)
elif cnt1 == 0 and cnt2 == 0:
    print(4)
