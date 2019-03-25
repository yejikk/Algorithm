import sys
sys.stdin = open('숫자찾기.txt')

def number_find(s, e, data):
    global N, number

    while s <= e:
        mid = (s + e) // 2
        if data < number[mid]:
            e = mid - 1

        elif data > number[mid]:
            s = mid + 1

        elif data == number[mid]:
            return mid
    return -1

N = int(input())
number = list(map(int, input().split()))
T = int(input())
find = list(map(int, input().split()))

for i in range(T):
    sol = number_find(0, N-1, find[i])
    print(sol+1)