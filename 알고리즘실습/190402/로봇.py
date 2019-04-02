import sys
sys.stdin = open('로봇.txt')

N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

sx, sy, si = map(int, input().split())
ex, ey, ei = map(int, input().split())