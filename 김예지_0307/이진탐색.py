import sys
sys.stdin = open('이진탐색.txt')

def inorder(n):
    global number, num, N
    if n != 0:
        inorder(first[n])
        number[n] = num
        num += 1
        inorder(second[n])
    return number

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    first = [0] * (N+2)
    second = [0] * (N+2)
    number = [0] * (N+2)
    num = 1
    for i in range(1, (N//2)+1):
        if i*2 > N:
            first[i] = 0
        else:
            first[i] = i*2
        if i*2+1 > N:
            second[i] = 0
        else:
            second[i] = i*2+1

    result = inorder(1)
    print('#' + str(tc), end=' ')
    print(result[1], end=' ')
    print(result[N//2])
