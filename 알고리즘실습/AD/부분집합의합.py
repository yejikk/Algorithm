import sys
sys.stdin = open('부분집합의합.txt')

def subset(number):
    # 원소의 수 -> S
    # 원소의 수가 S개 일 경우 2**S는 전체 부분집합의 수를 의미(공집합 포함)
    arr = [[] for _ in range(2**S)]

    # 부분집합의 개수
    for i in range(1<<S):
        # 원소의 수만큼 비트 비교
        for j in range(S):
            if i & (1<<j):
                arr[i].append(number[j])

    return arr

T = int(input())

for tc in range(1, T+1):
    S = 12
    N, K = map(int, input().split())

    number = list(map(int, range(1, S+1)))

    setarr = subset(number)
    flag = 0
    cnt = 0

    for i in range(len(setarr)):
        if len(setarr[i]) == N and sum(setarr[i]) == K:
            cnt += 1

    if cnt > 0:
        print('#{} {}'.format(tc, cnt))
    else:
        print('#{} {}'.format(tc, 0))