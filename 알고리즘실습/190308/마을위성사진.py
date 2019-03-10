import sys
sys.stdin = open('마을위성사진.txt')

N = int(input())
arr = [[0]*N for _ in range(N)]
for k in range(N):
    arr[k] = list(map(int, input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for height in range(1, N+1):
    check = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            flag = 0
            if arr[i][j] == height:
                for l in range(4):
                    tx = i + dx[l]
                    ty = j + dy[l]
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

result = 0
for x in range(N):
    for y in range(N):
        if arr[x][y] > result:
            result = arr[x][y]
print(result)