import sys
sys.stdin = open('그래프경로.txt')

def dfs(v): # 경로 찾는 함수
    stack.append(v)
    while len(stack) != 0:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in range(1, V+1):
                if route[v][w] == 1 and not visited[w]:
                    stack.append(w)
    return

test = int(input())

for tc in range(1, test+1):
    V, E = map(int, input().split()) # 노드, 간선

    # 경로를 나타내는 배열 선언하기
    route = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        node, line = map(int, input().split())
        route[node][line] = 1

    start, end = map(int, input().split()) # 시작, 끝

    visited = [0] * (V+1) # 방문했는지 안했는지 check해줄 list
    stack = [] # push, pop을 해줄 stack list 생성
    dfs(start) # 시작을 dfs 함수에 넣어준다.

    # 만약에 start에서 시작해서 end를 방문했다면 1이 되기 때문에 1이면 경로 존재 0이면 경로 존재 안함
    if visited[end] == 1: 
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')