import sys
sys.stdin = open("max_min.txt")

test = int(input())
for tc in range(test):
    N = int(input())
    number = list(map(int, input().split()))
    max_num = 0
    min_num = 98798754
    for i in range(N):
        if number[i] > max_num:
            max_num = number[i]
        if number[i] < min_num:
            min_num = number[i]
    print(f'#{tc+1} {max_num - min_num}')