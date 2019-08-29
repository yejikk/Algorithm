import sys
sys.stdin = open('workshop.txt')

def perm(k):
    global nmax
    money = ''.join(map(str, num))
    money = int(money)

    # 메모이제이션을 이용해서 가지치기
    if money in memo[k]:
        return
    else:
        memo[k].append(money)

    # 완성된거 비교해주기
    if cnt == k:
        if money > nmax:
            nmax = money
        return

    else:
        for i in range(N-1):
            for j in range(i+1, N):
                num[i], num[j] = num[j], num[i]
                perm(k+1)
                num[i], num[j] = num[j], num[i]

test = int(input())

for tc in range(1, test+1):
    num, cnt = map(str, input().split())
    num = list(map(int, num))
    N = len(num)
    temp = [0] * N
    cnt = int(cnt)
    nmax = 0
    memo = [[] for _ in range(cnt+1)] # 메모이제이션
    perm(0)
    print('#{} {}'.format(tc, nmax))

