import sys
sys.stdin = open('노드의거리.txt')

def bfs(v):
    global G, V
    visited = [0] * (V+1)
    queue=[]
    queue.append(v)
    while len(queue) != 0:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            for w in range(1, V+1):
                if G[v][w] == 1 and visited[w] == 0:
                    queue.append(w)


test = int(input())

for tc in range(1, test+1):
    N, M = map(int, input().split())
    node = [[0]*(N+1) for _ in range(N+1)]

    for i in range(M):
        x, y = map(int, input().split())
        node[x][y] = 1
        node[y][x] = 1

    start, end = map(int, input().split())
    bfs(start)