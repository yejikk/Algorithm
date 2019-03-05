import sys
sys.stdin = open('노드.txt')

def bfs(v):
    global node, N, end
    visited = [0] * (N+1)
    cnt = 0
    queue = []
    queue.append(v)
    while queue:
        v = queue.pop()


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