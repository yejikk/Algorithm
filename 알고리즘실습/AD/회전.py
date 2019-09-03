import sys
sys.stdin = open('회전.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    while M:
        num = number.pop(0)
        number.append(num)
        M -= 1

    print('#{} {}'.format(tc, number[0]))