import sys
sys.stdin = open('이진탐색.txt')

def binary(P, page):
    start = 0
    end = P
    cnt = 0
    binary_page = 1

    while binary_page > 0:
        binary_page = (start + end) // 2

        if binary_page == page:
            break

        if page > binary_page:
            start = binary_page
            cnt += 1

        else:
            end = binary_page
            cnt += 1

    return cnt

T = int(input())

for tc in range(1, T+1):
    P, PA, PB = map(int, input().split())

    A = binary(P, PA)
    B = binary(P, PB)

    if A == B:
        print('#{} {}'.format(tc, 0))

    elif A < B:
        print('#{} A'.format(tc))

    else:
        print('#{} B'.format(tc))