import sys
sys.stdin = open('shuffle.txt')

def shuffle(left, right):
    s_card = card
    flag = 0
    cnt = 0
    L_idx = len(left) -1
    R_idx = N // 2

    for i in range(N):
        if i < N//2:
            for j in range(i):
                temp = left[L_idx]
                left[L_idx] = right[j]
                right[j] = temp
                s_card = left + right
                print(s_card)

        if s_card == sort_card or s_card == reverse_card:
            flag = 1
            break
        else:
            cnt += 1

    if flag:
        return cnt
    else:
        return -1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    left_card = card[:N//2]
    right_card = card[N//2:]
    sort_card = sorted(card)
    reverse_card = sorted(card, reverse=True)

    result = shuffle(left_card, right_card)
    print('#{} {}'.format(tc, result))