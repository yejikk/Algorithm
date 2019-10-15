import sys
sys.stdin = open('DFS와BFS.txt')

def dfs(v):
    global N, M, node, V, visited, dfs_result
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs_result.append(v)
            visited[v] = 1
            for w in range(1, N+1):
                if node[v][w] and not visited[w]:
                    dfs(w)

    return ' '.join(map(str, dfs_result))

def bfs(v):
    global N, M, node, V, visited, bfs_result
    queue = [v]
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            bfs_result.append(v)
            for w in range(1, N+1):
                if node[v][w] and not visited[w]:
                    queue.append(w)

    return ' '.join(map(str, bfs_result))

N, M, V = map(int, input().split())
node = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    n, m = map(int, input().split())
    node[n][m] = 1
    node[m][n] = 1

visited = [0] * (N+1)
dfs_result = []
print(dfs(V))

visited = [0] * (N+1)
bfs_result = []
print(bfs(V))