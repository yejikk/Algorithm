import sys
sys.stdin = open("d3-2.txt")

test = int(input())

for tc in range(1, test+1):
    score = list(map(int, input().split()))
    sum = 0
    for num in score:
        if num < 40:
           sum += 40
        else:
            sum += num

    print(f'#{tc} {sum // 5}')
