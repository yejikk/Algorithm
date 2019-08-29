# c 버전에서는 stack 안의 값들이 계속 남아있음
# c는 배열의 크기가 한정적임(100이라고 해놓으면 100이상 쓸 수 없다는 단점이 있다.)
size = 100
stack = [0] * size # stack 안의 값들이 계속 남아있기 때문에 top이 필요함
top = -1 # top이 왜 필요한지 이유를 제대로 알고 있어야함
def push(item):
    global top, stack
    if top >= size-1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top, stack
    if top == -1:
        print("Stack is empty!")
        return
    else:
        result = stack[top]
        top -= 1
        return result

push(1)
push(2)
push(3)
item = pop()
print('pop item => %d' %item)
item = pop()
print('pop item => %d' %item)
item = pop()
print('pop item => %d' %item)
print(top)
print(stack) # stack 안의 값들이 계속 남아있음