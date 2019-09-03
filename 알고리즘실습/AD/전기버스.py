import sys
sys.stdin = open('전기버스.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus = list(map(int, range(N+1)))
    stop = list(map(int, input().split()))
    charge = list(map(int, range(N+1)))

    for n in stop:
        charge[n] = 999

    flag = 1
    idx = K
    cnt = 0

    while flag:
        if idx >= N:
            flag = 1
            break

        if idx <= N and charge[idx] == -1:
            flag = 0
            break

        if charge[idx] == 999:
            cnt += 1
            charge[idx] = -1
            idx += K

        else:
            idx -= 1

    if flag:
        print('#{} {}'.format(tc, cnt))
    else:
        print('#{} {}'.format(tc, 0))