import sys
sys.stdin = open('캐슬디펜스.txt')

N, M, D = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))
    print(arr[i])