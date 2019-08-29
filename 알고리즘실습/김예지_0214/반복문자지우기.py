import sys
sys.stdin = open('반복문자지우기.txt')

test = int(input())

def push(item):
    stack.append(item)

def pop():
    result = stack.pop()
    return result

def isempty():
    if len(stack) == 0:
        return False
    else:
        return True

for tc in range(1, test+1):
    string = input()
    stack = [string[0]]
    i = 1

    for i in range(1, len(string)):
        if isempty():
            if stack[-1] != string[i]:
                push(string[i])
            else:
                pop()
        else:
            push(string[i])

    print(f'#{tc} {len(stack)}')