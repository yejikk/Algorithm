import sys
sys.stdin = open('암호문3.txt')

for tc in range(1, 11):
    N = int(input())
    original = list(input().split())
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
                original.pop()
        elif secret[i] == 'A':
            num = int(secret[i+1])
            for l in range(num):
                original.append(secret[i+2+l])

    original = ' '.join(original[:10])
    print(f'#{tc} {original}')