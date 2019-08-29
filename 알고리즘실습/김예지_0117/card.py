import sys
sys.stdin = open("card.txt")

T = int(input())

for tc in range(T):
    card = int(input())
    num = list(map(int, input()))

    cnt = [0] * 10
    max = 0
    for i in range(len(num)):
        cnt[num[i]] += 1
    for j in range(len(cnt)):
        if cnt[j] >= max:
            max = cnt[j]
            result = j
    print(f'#{tc+1} {result} {max}')