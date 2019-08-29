import sys
sys.stdin = open("section_sum.txt")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    M_max = 0
    M_min = 99999999

    for i in range(M-1, N):
        M_sum = 0
        for j in range(1, M):
            M_sum += number[i-j]
        M_sum += number[i]
        if M_sum > M_max:
            M_max = M_sum
        if M_sum < M_min:
            M_min = M_sum
    print(f'#{tc+1} {M_max - M_min}')