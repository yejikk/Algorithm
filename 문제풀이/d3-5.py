# 세가지 합 구하기

import sys
sys.stdin = open("d3-5.txt")

test = int(input())

for tc in range(1, test+1):
    N = int(input())

    numbers = list(range(1, (2*N)+1))
    s1 = sum(numbers[:N])
    s2 = sum(numbers[::2])
    s3 = sum(numbers[1::2])
    print(f'#{tc} {s1} {s2} {s3}')