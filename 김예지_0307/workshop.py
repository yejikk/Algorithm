import sys, pprint
sys.stdin = open('workshop.txt')

def postorder(node):
    global stack
    if node != 0:
        postorder(tree[node][1])
        postorder(tree[node][2])
        stack.append(tree[node][0])

def calculator(stack):
    number = []
    for cal in stack:
        if type(cal) == int:
            number.append(cal)
        else:
            if cal == '-':
                num2 = number.pop()
                num1 = number.pop()
                sub = num1 - num2
                number.append(sub)
            elif cal == '+':
                num2 = number.pop()
                num1 = number.pop()
                add = num1 + num2
                number.append(add)
            elif cal == '*':
                num2 = number.pop()
                num1 = number.pop()
                mul = num1 * num2
                number.append(mul)
            elif cal == '/':
                num2 = number.pop()
                num1 = number.pop()
                div = num1 // num2
                number.append(div)
    return number

for tc in range(1, 11):
    stack = []
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    for i in range(N):
        temp = list(map(str, input().split()))
        temp[0] = int(temp[0])
        if len(temp) == 4:
            tree[temp[0]][0] = temp[1]
            tree[temp[0]][1] = int(temp[2])
            tree[temp[0]][2] = int(temp[3])
        elif len(temp) == 2:
            tree[temp[0]][0] = int(temp[1])

    postorder(1)
    result = calculator(stack)
    print('#' + str(tc) + ' ' + str(result[-1]))