import sys
sys.stdin = open('글자수.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    word = {}

    for text in str1:
        word[text] = 0

    for s in str2:
        if s in word:
            word[s] += 1

    cnt = 0
    for key in word:
        if word[key] > cnt:
            cnt = word[key]

    print('#{} {}'.format(tc, cnt))