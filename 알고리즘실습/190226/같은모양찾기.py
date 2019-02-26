import sys
sys.stdin = open('같은모양찾기.txt')

def rotation(pattern, m, k):
    if k == 0:
        return pattern
    else:
        for l in range(k):
            newpattern = [[] for _ in range(m)]
            for i in range(m):
                for j in range(m-1, -1, -1):
                    newpattern[i].append(pattern[j][i])
            pattern = newpattern
        return newpattern

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

M = int(input())
pattern = [[0]*M for _ in range(M)]
for j in range(M):
    pattern[j] = list(map(int, input()))

sol = 0
for k in range(4):
    shape = rotation(pattern, M, k)
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for x in range(M):
                for y in range(M):
                    if arr[i+x][j+y] == shape[x][y]:
                        cnt += 1
                if cnt == M*M:
                    sol += 1
print(sol)
