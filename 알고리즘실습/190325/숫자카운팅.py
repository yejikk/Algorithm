import sys
sys.stdin = open('숫자카운팅.txt')

def lower(s, e, data):
    global number

    idx = -1
    while s <= e:
        mid = (s+e) // 2
        if data == number[mid]:
            e = mid - 1
            idx = mid

        elif data > number[mid]:
            s = mid + 1

        elif data < number[mid]:
            e = mid - 1
    return idx

def upper(s, e, data):
    global number

    idx = -1
    while s <= e:
        mid = (s + e) // 2

        if data == number[mid]:
            idx = mid
            s = mid + 1

        elif data > number[mid]:
            s = mid + 1

        elif data < number[mid]:
            e = mid - 1

    return idx

N = int(input())
number = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

for i in range(M):
    L = lower(0, N-1, find[i])
    if L >= 0:
        U = upper(0, N-1, find[i])
        print(U-L+1, end=' ')
    else:
        print(0, end=' ')