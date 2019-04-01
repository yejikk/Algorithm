import sys
sys.stdin = open('NQUEEN.txt')

# def check(r, c):
#     dc = [-1, 0, 1]
#     dr = [-1, -1, -1]
#     for i in range(3): # 3방향
#         for k in range(1, N): # 1배, 2배, ... 떨어진 거리
#             nr = r + dr[i] * k
#             nc = c + dc[i] * k
#             if nr < 0 or nr >= N or nc < 0 or nc >= N:
#                 break
#             if arr[nr][nc]:
#                 return 0
#
#     return 1

def DFS(no): # depth == 행
    global sol
    if no >= N:
        sol += 1
        return

    for i in range(N):
        if chk1[i]: # 세로방향체크
            continue
        if chk2[no+i]: # 우방향대각선체크
            continue
        if chk3[(N-1)-(no-i)]: # 좌방향대각선체크
            continue
        chk1[i] = chk2[no+i] = chk3[(N-1)-(no-i)] = 1 # 퀸놓기
        DFS(no+1)
        chk1[i] = chk2[no+i] = chk3[(N-1)-(no-i)] = 0 # 퀸빼기
        # if check(no, i):
        #     arr[no][i] = 1
        #     DFS(no+1)
        #     arr[no][i] = 0

N = int(input())
arr = [[0]*N for _ in range(N)]
chk1 = [0]*N
chk2 = [0]*N*2
chk3 = [0]*N*2
sol = 0
DFS(0)
print(sol)

