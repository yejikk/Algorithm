import pprint
import sys
sys.stdin = open('1260.txt')

# DFS - stack
def DFS(v):
    visited[v] = 1
    dfs_list.append(v)

    for w in range(1, N+1):
        if arr[v][w] == 1 and visited[w] == 0:
            DFS(w)

    return dfs_list

# BFS - queue
def BFS(v):
    q = []
    q.append(v)

    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            bfs_list.append(v)
            for w in range(1, N+1):
                if arr[v][w] == 1 and visited[w] == 0:
                    q.append(w)
    return bfs_list

# N: 정점의 개수, M: 간선의 개수, V: 시작 정점 번호
N, M, V = map(int, input().split())

# 배열에 간선에 연결하는 정점을 check
arr = [[0]*(N+1) for _ in range(N+1)]

# 결과값
dfs_list = []
bfs_list = []

for i in range(M):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

# 정점에 방문하였는지 check
visited = [0] * (N+1)
dfs_result = ' '.join(map(str, DFS(V)))

# 정점에 방문하였는지 check
visited = [0] * (N+1)
bfs_result = ' '.join(map(str, BFS(V)))

print(dfs_result)
print(bfs_result)
