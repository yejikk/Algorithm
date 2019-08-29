import sys, pprint
sys.stdin = open('workshop.txt')

def inorder(node):
    global result
    if node != 0:
        inorder(tree[node][2])
        result += tree[node][1]
        inorder(tree[node][3])
    return result

for tc in range(1, 11):
    N = int(input())
    temp = []
    tree = [[0]*4 for i in range(N+1)]
    result = ''

    for i in range(N):
        temp.append(list(input().split()))

    for i in range(N):
        if len(temp[i]) == 4:
            tree[i+1] = temp[i]
            tree[i+1][2] = int(tree[i+1][2])
            tree[i+1][3] = int(tree[i+1][3])
        elif len(temp[i]) == 3:
            tree[i+1] = temp[i]
            tree[i+1][2] = int(tree[i+1][2])
            tree[i+1].append(0)
        elif len(temp[i]) == 2:
            tree[i+1] = temp[i]
            tree[i+1].append(0)
            tree[i+1].append(0)

    result = inorder(1)
    print(f'#{tc} {result}')