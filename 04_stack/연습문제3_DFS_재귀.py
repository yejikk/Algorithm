import sys
sys.stdin = open('연습문제3_input.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)] # 2차원 배열
visited = [0 for i in range(V+1)] # 방문했는지 check
stack = []

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(1, V+1):
    print(f'{i} {G[i]}')

dfs(1)
