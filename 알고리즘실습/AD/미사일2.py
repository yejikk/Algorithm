import sys
sys.stdin = open('미사일.txt')

def combi(x, y):
    global N
    if y == 0:
        print(t)
        for i in range(N):
            arr[i][2] = copy[i]

    elif x < y:
        return
    else:
        t[y-1] = arr[x-1]
        combi(x, y-1)
        combi(x-1, y)

N =int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M, B, D = map(int, input().split())
minN = 9999999999999
t = [0] * M
copy = [0] * N
for i in range(N):
    copy[i] = arr[i][2]
combi(N, M)
