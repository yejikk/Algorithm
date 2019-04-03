# 최소신장트리 구하는 법2
# KRUSKAL
import sys
sys.stdin = open('최소신장트리.txt')

def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])

def mst():
    global V
    cnt = 0 # 간선 개수
    total = 0 # 가중치의 합
    i = 0 # 제어변수
    while cnt < V: # MST 구성을 위해 v개의 간선을 선택
        p1 = findSet(edge[i][0]) # 두 노드의 대표원소 알아내기
        p2 = findSet(edge[i][1])
        if p1 != p2: # 사이클이 생성되지 않으면
            total += edge[i][2] # MST에 포함되므로 가중치 추가
            cnt += 1
            p[p2] = p1
        i += 1
    return total

test = int(input())

for tc in range(1, test+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for i in range(E)]
    edge.sort(key=lambda x : x[2])
    p = list(range(V+1))

    # print(edge)
    print(mst())