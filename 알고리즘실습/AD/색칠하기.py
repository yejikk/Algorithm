import sys
sys.stdin = open('색칠하기.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*10 for _ in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color

    cnt = 0
    for x in range(10):
        for y in range(10):
            if arr[x][y] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
