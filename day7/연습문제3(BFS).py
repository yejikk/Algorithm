def BFS(v):
    queue.append(v)
    visited[v] = 1
    print(v, end=' ')
    while queue:
        t = queue.pop(0)
        # if not visited[t]:
        #     visited[t] = True
        #     print(t, end=' ')
        for i in range(1, len(arr[t])):
            if arr[t][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
                print(i, end=' ')

N, M = 7, 8
line = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

arr = [[0]* (N+1) for _ in range(N+1)]
visited = [0]*M
queue = []

for i in range(0, len(line), 2):
    arr[line[i]][line[i+1]] = 1
    arr[line[i+1]][line[i]] = 1

# for i in range(M):
#     print(i, arr[i])

BFS(1)
print(visited)