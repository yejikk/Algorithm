import sys
sys.stdin = open('암호문1.txt')

for tc in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))
    M = int(input())
    secret = list(input().split())

    for i in range(len(secret)):
        if secret[i] == 'I':
            idx = int(secret[i+1])
            if idx >= N:
                continue
            else:
                num = int(secret[i+2])
                for j in range(i+3, i+3+num):
                    original[idx] = secret[j]
                    idx += 1
                    if idx >= N:
                        break

    original = ' '.join(map(str, original[:10]))
    print(f'#{tc} {original}')

