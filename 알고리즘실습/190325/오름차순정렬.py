import sys
sys.stdin = open('오름차순정렬.txt')

def sort():
    global N, number
    for i in range(N-1):
        for j in range(i, N):
            if number[i] > number[j]:
                number[i], number[j] = number[j], number[i]
    return number

N = int(input())
number = list(map(int, input().split()))
sort()

print(' '.join(map(str, number)))