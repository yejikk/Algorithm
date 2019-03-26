# 이차원 배열 - BFS 순열 연습 (문제는 가지치기 해줘야지 풀림)
import sys
sys.stdin = open('최소의합.txt')

# 현재 행에 모든 열의 수를 고르는 경우의 수 시도
def DFS1(no, nsum):
    global sol
    if nsum > sol: # 가지치기
        return

    if no >= N:
        # 기록한 것 print
        # for i in range(N):
        #     print(rec[i], end=' ')
        # print(nsum)

        if nsum < sol:
            sol = nsum
        return

    for i in range(N): # 열요소
        rec[no] = arr[no][i]
        DFS1(no+1, nsum + arr[no][i])

# 현재 행에서 모든 열의 수를 고르는 경우의 수 시도 단, 열의 중복 배제
def DFS2(no, nsum):
    global sol
    if nsum > sol:  # 가지치기
        return

    if no >= N:
        # 기록한 것 print
        # for i in range(N):
        #     print(rec[i], end=' ')
        # print(nsum)

        if nsum < sol:
            sol = nsum
        return

    # 현재 행에 모든 열의 수를 고르는 경우의 수 시도
    for i in range(N):  # 열요소
        if chk[i] == 1:
            continue
        chk[i] = 1
        rec[no] = arr[no][i]
        DFS2(no + 1, nsum + arr[no][i])
        chk[i] = 0
    # 다 끝나면 return

N = int(input())

chk = [0] * 11 # 열의 중복을 체크할 배열
rec = [0] * 11 # 조합된 결과를 기록할 배열

arr = [[0]*N for _ in range(N)]
for k in range(N):
    arr[k] = list(map(int, input().split()))

sol = 10000000
DFS1(0, 0)
print(sol)

sol = 10000000
DFS2(0, 0)
print(sol)