import sys
sys.stdin = open('2048.txt')

def solution(cnt):
    global N, arr, result
    if cnt == 5:
        for i in range(N):
            result = max(result, arr[i])
        return

    temp = [x[:] for x in arr]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

solution(0)
