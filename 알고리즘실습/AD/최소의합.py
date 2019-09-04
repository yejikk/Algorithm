import sys
sys.stdin = open('최소의합.txt')

def dfs(n, sums):
    global min_dfs

    if sums > min_dfs:
        return

    if n >= N:
        if sums < min_dfs:
            min_dfs = sums
        return

    for i in range(N):
        dfs(n+1, sums+arr[n][i])

def dfs2(n, sums):
    global min_dfs2

    if sums > min_dfs2:
        return

    if n >= N:
        if sums < min_dfs2:
            min_dfs2 = sums

    for i in range(N):
        if chk[i]:
            continue
        chk[i] = 1
        dfs2(n+1, sums+arr[n][i])
        chk[i] = 0

N = int(input())
arr = [[0]*N for _ in range(N)]
rec = [0] * N
chk = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))

min_dfs = 99999999
dfs(0, 0)

min_dfs2 = 99999999
dfs2(0, 0)

print(min_dfs)
print(min_dfs2)