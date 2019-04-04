import sys
sys.stdin = open('로봇과자먹기.txt')

def DFS(no, nsum):
    global nmin
    if nsum > nmin:
        return

    if no == N:
        if nsum < nmin:
            nmin = nsum
        return
    for i in range(N):
        if chk[i] == 1:
            continue
        chk[i] = 1
        DFS(no+1, nsum + arr[no][i])
        chk[i] = 0

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    s = list(map(int, input().split()))
    r = list(map(int, input().split()))
    snack = []
    robot = []
    arr = [[0]*N for _ in range(N)]
    for i in range(0, N*2, 2):
        snack.append([s[i], s[i+1]])
        robot.append([r[i], r[i+1]])

    # 거리 계산해서 행렬에 넣어주기
    for i in range(N):
        for j in range(N):
            di = abs(robot[i][0] - snack[j][0]) + abs(robot[i][1] - snack[j][1])
            arr[i][j] = di

    chk = [0]*N
    nmin = 10000000
    DFS(0, 0)
    print(nmin)