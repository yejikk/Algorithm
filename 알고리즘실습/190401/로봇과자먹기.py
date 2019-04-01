import sys
sys.stdin = open('로봇과자먹기.txt')

def DFS(n, sums):
    global mins
    if n == N:
        if mins > sums:
            mins = sums
        return
    if sums > mins:
        return
    for i in range(N):
        if chk[i] == 0:
            chk[i] = 1
            DFS(n+1, sums + arr[n][i])
            chk[i] = 0

T = int(input())

for ti in range(T):
    N = int(input())
    snack = list(map(int, input().split()))
    robot = list(map(int, input().split()))

    chk = [0] * N
    arr = [[0]*N for _ in range(N)]
    mins = 10000000000000
    for i in range(N): # 행을 로봇
        for j in range(N): # 열을 과자
            di = abs(robot[i*2] - snack[j*2]) + abs(robot[i*2+1] - snack[j*2+1])
            arr[i][j] = di # 로봇별 과자와의 거리 기록
    DFS(0, 0) # 0번 로봇부터 시작, 합계0
    print(mins)