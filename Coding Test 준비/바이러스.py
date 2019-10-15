import sys
sys.stdin = open('바이러스.txt')

def dfs(v):
    global N, cnt
    visited[v] = 1
    for w in range(1, N+1):
        if node[v][w] and not visited[w]:
            cnt += 1
            dfs(w)

    return cnt

N = int(input())
M = int(input())

node = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    n, m = map(int, input().split())
    node[n][m] = 1
    node[m][n] = 1

cnt = 0
visited = [0] * (N+1)
print(dfs(1))

