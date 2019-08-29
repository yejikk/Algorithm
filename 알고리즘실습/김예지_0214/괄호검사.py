import sys
sys.stdin = open('괄호검사.txt')

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

def check(string):
    for char in string:
        if char == '(' or char == '{':
            push(char)

        elif char == ')':
            if isempty():
                element = pop()
                if element == '{':
                    return '0'
            else:
                return '0'
        elif char == '}':
            if isempty():
                element = pop()
                if element == '(':
                    return '0'
            else:
                return '0'

    if stack:
        return '0'
    else:
        return '1'

test = int(input())

for tc in range(1, test+1):
    string = input()
    stack = []

    result = check(string)

    print(f'#{tc} {result}')