import sys
sys.stdin=open("workshop.txt")

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    stick = [[0 for _ in range(2)] for _ in range(N)]

    for i in range(len(numbers)):
        j = i//2
        k = i%2
        stick[j][k] = numbers[i]
    print(stick)

    for

