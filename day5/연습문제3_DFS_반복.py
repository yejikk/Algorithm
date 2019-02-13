import sys
sys.stdin = open('연습문제3_input.txt')

def dfs(v):
    stack.append(v)
    while len(stack) != 0:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in range(1, V+1): # range 기억하기
                if G[v][w] == 1 and not visited[w]: # 행과 열 구분 잘해야함
                    stack.append(w)
    return

# 행이 어떤 역할인지, 열이 어떤 역할인지!!

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

'''
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2+1]] = 1
'''
