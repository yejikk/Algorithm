import sys
sys.stdin = open('로봇과자먹기.txt')

def dfs(no, nsum):
    global num_min

    if nsum > num_min:
        return

    if no >= N:
        if nsum < num_min:
            num_min= nsum
        return

    for i in range(N):
        if chk[i]:
            continue
        chk[i] = 1
        dfs(no+1, nsum+arr[no][i])
        chk[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*100 for _ in range(100)]

    chk = [0]*N
    arr = [[0]*N for _ in range(N)]

    robot = list(map(int, input().split()))
    snack = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            di = abs(robot[i*2] - snack[j*2]) + abs(robot[i*2+1] - snack[j*2+1])
            arr[i][j] = di

    num_min = 9999999999
    dfs(0, 0)
    print(num_min)