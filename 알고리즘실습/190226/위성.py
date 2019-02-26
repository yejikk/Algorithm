import sys
sys.stdin = open('위성.txt')

N = int(input())
arr = [[0]*N for _ in range(N)]

check = 0
flag = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    arr[i] = list(map(int, input()))

if arr:
    for height in range(1, N):
        check = 0
        for i in range(1, N-1):
            for j in range(1, N-1):
                flag = 0
                if arr[i][j] == height:
                    for k in range(4):
                        tx = i + dx[k]
                        ty = j + dy[k]
                        if arr[tx][ty] >= height:
                            flag = 1
                        else:
                            flag = 0
                            break
                if flag:
                    arr[i][j] += 1
                    check = 1
        if check == 0:
            break
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > cnt:
                cnt = arr[i][j]
    print(cnt)
else:
    print(0)

