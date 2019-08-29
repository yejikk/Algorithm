import sys, pprint
sys.stdin = open('workshop2.txt')

def common(node1_p,node2_p):
    flag = 0
    for x in range(len(node1_p)):
        for y in range(len(node2_p)):
            if node1_p[x] == node2_p[y]:
                result = node1_p[x]
                flag = 1
                break
        if flag:
            break
    return result

def preorder(node):
    global cnt
    if node != 0:
        preorder(tree[node][0])
        preorder(tree[node][1])
        cnt += 1
    return cnt

test = int(input())

for tc in range(1, test+1):
    V, E, node1, node2 = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(V+1)]
    cnt = 0

    for i in range(E):
        n1 = temp[i*2]
        n2 = temp[i*2+1]
        if tree[n1][0] == 0:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n1][2] = n1

    i = 0
    node1_p = []
    node2_p = []
    while True:
        for i in range(V+1):
            if tree[i][0] == node1 or tree[i][1] == node1:
                node1 = tree[i][2]
                node1_p.append(tree[i][2])

        if node1_p[-1] == 1:
            break

    while True:
        for j in range(V+1):
            if tree[j][0] == node2 or tree[j][1] == node2:
                node2 = tree[j][2]
                node2_p.append(tree[j][2])

        if node2_p[-1] == 1:
            break

    result = common(node1_p, node2_p)
    cnt = preorder(result)

    print(f'#{tc} {result} {cnt}')