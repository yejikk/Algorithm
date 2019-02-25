import sys
sys.stdin = open('회전.txt')

def sqaure_rotation(n, arr, cnt):
    while cnt:
        newarr = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n-1, -1, -1):
                newarr[i].append(arr[j][i])
        arr = newarr
        cnt -= 1
    return arr

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

while True:
    rotation = int(input())
    if rotation:
        cnt = rotation // 90
        result = sqaure_rotation(N, arr, cnt)
        for i in range(N):
            print(' '.join(map(str, result[i])))
        arr = result
    else:
        break