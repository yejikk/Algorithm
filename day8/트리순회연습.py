import sys, pprint
sys.stdin = open('트리순회연습.txt')

def printTree():
    for i in range(1, V+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))

def preorder(node):  # 전위 순회
    if node != 0:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):  # 중위 순회
    if node != 0:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])

def postorder(node):  # 후위 순회
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=' ')

V, E = map(int, input().split())
tree = [[0 for _ in range(3)] for _ in range(V+1)]  # Left, Right, Parent
temp = list(map(int, input().split()))

for i in range(E):
    n1 = temp[i * 2]  # Parent(n1)
    n2 = temp[i * 2 + 1]  # Child(n2)
    if tree[n1][0] == 0:  # Parent의 Left Child가 비어있으면 값을 삽입
        tree[n1][0] = n2
    else:  # Parent의 Right Child가 비어있으면 값을 삽입
        tree[n1][1] = n2
    tree[n2][2] = n1  # Child의 Parent에 값을 삽입

# print(V, E)
pprint.pprint(tree)
# print(temp)
printTree()

# preorder(1)