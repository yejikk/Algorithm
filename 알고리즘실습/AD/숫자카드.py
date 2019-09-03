import sys
sys.stdin = open('숫자카드.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()
    cnt = [0] * 10

    for card in cards:
        n = int(card)
        cnt[n] += 1

    idx = 0
    num = 0
    for i in range(len(cnt)):
        if cnt[i] > num:
            num = cnt[i]
            idx = i

        elif cnt[i] == num:
            if i > idx:
                idx = i
                num = cnt[i]

    print('#{} {} {}'.format(tc, idx, num))
