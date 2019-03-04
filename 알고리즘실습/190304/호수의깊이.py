import sys
sys.stdin = open('호수의깊이.txt')

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(1, N-1):
    for j in range(1, N-1):
        cnt = 0
        k = 1
        if arr[i][j] != 0:
            while True:
                if arr[i][j-k] == 0 or arr[i-k][j] == 0 or arr[i+k][j] == 0 or arr[i][j+k] == 0:
                    cnt += 1
                    break
                else:
                    k += 1
                    cnt += 1
            arr[i][j] = cnt

result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            result += arr[i][j]
print(result)
