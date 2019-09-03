import sys
sys.stdin = open('노드의거리.txt')

def bfs(start, end):
    queue = []
    queue.append(start)

    while queue:
        v = queue.pop(0)
        if v == end:
            return visited[v]
            break

        for w in range(1, V+1):
            if arr[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1

    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)

    for n in range(E):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    start, end = map(int, input().split())

    result = bfs(start, end)
    print('#{} {}'.format(tc, result))