import sys
sys.stdin = open('오름차순정렬.txt')

def Qsort(s, e): # start, end
    global N, number
    if s >= e:
        return
    P = e
    T = s
    for L in range(s, e+1):
        if number[L] < number[P]:
            number[L], number[T] = number[T], number[L]
            T += 1
    number[T], number[P] = number[P], number[T]
    Qsort(s, T-1)
    Qsort(T+1, e)

N = int(input())
number = list(map(int, input().split()))
Qsort(0, N-1)

print(' '.join(map(str, number)))