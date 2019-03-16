import sys
sys.stdin = open('암호문2.txt')

for tc in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))
    M = int(input())
    secret = list(input().split())
    for i in range(len(secret)):
        if secret[i] == 'I':
            idx = int(secret[i+1])
            num = int(secret[i+2])
            for j in range(i+3, i+3+num):
                original.insert(idx, secret[j])
                idx += 1

        elif secret[i] == 'D':
            idx = int(secret[i+1])
            num = int(secret[i+2])
            for k in range(num):
                original.pop(idx)

    original = ' '.join(map(str, original[:10]))
    print(f'#{tc} {original}')