import sys
sys.stdin = open('같은모양찾기simple.txt')

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

M = int(input())
pattern = [[0]*M for _ in range(M)]
for j in range(M):
    pattern[j] = list(map(int, input()))

sol = 0
for i in range(N-M+1): # 모눈종이 행제어
    for j in range(N-M+1): # 모눈종이 열 제어
        cnt = 0
        for x in range(M):# 패턴의 행
            for y in range(M): # 패턴의 열
                if arr[i+x][j+y] == pattern[x][y]:
                    cnt += 1
            if cnt == M*M:
                sol += 1
print(sol)