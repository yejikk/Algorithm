import sys
sys.stdin = open('1226.txt')

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack.append([x, y])

    # while stack:


T = 10

for _ in range(1, T+1):
    tc = int(input())
    N = 16
    arr = [[0]*N for _ in range(N)]

    stack = []
    visited = []

    for n in range(N):
        arr[n] = list(map(int, input()))
        print(arr[n])

    flag = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = i
                y = j
                flag = 1
                break
        if flag:
            break

