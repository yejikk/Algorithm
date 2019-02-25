import sys
sys.stdin = open('배열정리.txt')

N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(N):
    cnt = 1
    for j in range(1, M):
        if arr[i][j-1] == 1 and arr[i][j] == 1:
            cnt += 1
            arr[i][j] = cnt
        elif arr[i][j-1] > arr[i][j] and arr[i][j] == 1:
            cnt += 1
            arr[i][j] = cnt
        elif arr[i][j] == 0:
            cnt = 1
            continue

for i in range(N):
    print(' '.join(map(str, arr[i])))