import sys
sys.stdin = open('노드의합.txt')

def order(node):
    global N
    if node != N:
        if node * 2 <= N:
            tree[node][0] = node * 2
            tree[node*2][2] = node
        if node * 2 + 1 <= N:
            tree[node][1] = node * 2 + 1
            tree[node*2+1][2] = node
        node += 1
        order(node)

def postorder(node):
    global N
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        tree[node // 2][3] += tree[node][3]

test = int(input())
for tc in range(1, test+1):
    N, M, L = map(int, input().split())
    tree = [[0, 0, 0, 0] for i in range(N+1)]
    for i in range(M):
        N1, N2 = map(int, input().split())
        tree[N1][3] = N2

    order(1)
    postorder(1)
    print('#' + str(tc) + ' ' + str(tree[L][3]))
