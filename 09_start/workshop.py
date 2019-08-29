import sys
sys.stdin = open('workshop.txt')

def binary(secret):
    global pattern
    result = []
    for i in range(0, len(secret), 7):
        simple = secret[i:i+7]
        for j in range(len(pattern)):
            if pattern[j] == simple:
                result.append(j)
    return result

test = int(input())

for tc in range(1, test+1):
    N, M = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for k in range(N):
        arr[k] = list(map(int, input()))

    pattern = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1],
               [0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1],
               [0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1],
               [0, 0, 0, 1, 0, 1, 1]]
    flag = 0
    secret = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                for l in range(j-55, j+1):
                    secret.append(arr[i][l])
                flag = 1
                break
            if flag:
                break
    code = binary(secret)

    odd = (code[0] + code[2] + code[4] + code[6]) * 3
    even = code[1] + code[3] + code[5]
    result = odd + even + code[7]

    if result % 10 == 0:
        print('#{} {}'.format(tc, sum(code)))
    else:
        print('#{} 0'.format(tc))