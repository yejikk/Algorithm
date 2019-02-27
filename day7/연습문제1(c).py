SIZE = 100
Q = [0] * SIZE
front, rear = -1, -1

def isFull():
    global rear
    if rear == len(Q)-1:
        return True
    else:
        False

def isEmpty():
    global front, rear
    if front == rear:
        return False
    else:
        return True

def enQueue(item):
    global rear
    if isEmpty():
        rear += 1
        Q[rear] = item

def deQueue():
    if isEmpty():
        Q.pop(0)

def Qpeek():
    global front
    return Q[front+1]


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
