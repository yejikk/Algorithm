import sys
sys.stdin = open('회전.txt')

test = int(input())

for tc in range(1, test+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    for i in range(M):
        p = number.pop(0)
        number.append(p)

    print(f'#{tc} {number[0]}')