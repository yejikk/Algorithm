import sys
sys.stdin = open('구간합.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    num_min = 99999999999
    num_max = 0
    for i in range(N-M+1):
        num_sum = 0
        for j in range(i, i+M):
            num_sum += nums[j]

        if num_sum < num_min:
            num_min = num_sum

        if num_sum > num_max:
            num_max = num_sum

    print('#{} {}'.format(tc, num_max - num_min))
