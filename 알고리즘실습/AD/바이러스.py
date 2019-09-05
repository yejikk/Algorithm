import sys
sys.stdin = open('바이러스.txt')

def dfs(v):
    global cnt

    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            cnt += 1
            for w in range(1, V+1):
                if not visited[w] and temp[v][w] == 1:
                    stack.append(w)
    return cnt

V = int(input())
E = int(input())

temp = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    x, y = map(int, input().split())
    temp[x][y] = 1
    temp[y][x] = 1

cnt = 0
visited = [0] * (V+1)
if sum(temp[1]) != 0:
    print(dfs(1)-1)
else:
    print(cnt)