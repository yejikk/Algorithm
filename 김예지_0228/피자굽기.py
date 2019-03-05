import sys
sys.stdin = open('피자굽기.txt')

test = int(input())

for tc in range(1, test+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    pizza = []
    for i in range(M):
        pizza.append([i+1, num[i]])

    queue = []
    for i in range(N):
        queue.append(pizza[i])

    for j in range(N):
        pizza.pop(0)

    while True:
        if len(queue) == 1:
            break
        elif len(queue) > 1:
            cheese = queue.pop(0)
            cheese[1] //= 2
            if pizza:
                if cheese[1] == 0:
                    queue.append(pizza[0])
                    pizza.pop(0)
                else:
                    queue.append(cheese)
            else:
                if cheese[1] == 0:
                    continue
                else:
                    queue.append(cheese)

    print('#'+ str(tc) + ' ' +str(queue[0][0]))
