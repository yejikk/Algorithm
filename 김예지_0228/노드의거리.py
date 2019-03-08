import sys
sys.stdin = open('노드의거리.txt')

def bfs(v):
    global node, visited, V, end
    queue = []
    queue.append(v)
    while len(queue) != 0:
        v = queue.pop(0)
        if v == end:
            return visited[v]
            break
        for w in range(1, V+1):
            if node[v][w] == 1 and not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1

test = int(input())

for tc in range(1, test+1):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    node = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        n, m = map(int, input().split())
        node[n][m] = 1
        node[m][n] = 1
    start, end = map(int, input().split())

    result = bfs(start)
    print('#' + str(tc) + ' ' + str(result))
