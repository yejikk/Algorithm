import sys, pprint
sys.stdin = open('subtree.txt')

def preorder(n):
    global cnt
    if n != 0:
        cnt += 1
        preorder(tree[n][0])
        preorder(tree[n][1])
    return cnt

test = int(input())

for tc in range(1, test+1):
    E, N = map(int, input().split())
    tree = [[0]*3 for _ in range(E+2)]
    temp = list(map(int, input().split()))
    cnt = 0
    for i in range(E):
        n1 = temp[i*2]
        n2 = temp[i*2+1]
        if tree[n1][0] == 0:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1
    result = preorder(N)
    print('#' + str(tc) + ' ' + str(result))