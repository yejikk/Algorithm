# python
def push(item): # push 함수
    s.append(item) # append를 이용해서 list에 item(값)을 추가한다(push)

def pop(): # pop 함수
    if len(s) == 0: # list s의 len(s)가 0이면
        print("Stack is Empty!")
    else:
        return s.pop()

s = []

push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())