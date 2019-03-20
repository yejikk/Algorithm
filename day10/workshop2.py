import sys
sys.stdin = open('workshop2.txt')

test = int(input())

for tc in range(1, test+1):
    N, M = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for k in range(N):
        arr[k] = list(input())

    secret = []
    for i in range(N):
        s_code = ''
        flag = 0
        for j in range(M-1, -1, -1):
            s_code = ''
            if arr[i][j] != '0':
                ty2 = j+1
                for l in range(j, -1, -1):
                    if s_code != '' and s_code[0] == '0' and arr[i][l] == '0':
                        tx = i
                        ty = l+2
                        break
                    else:
                        s_code = arr[i][l] + s_code
                s_code = s_code[1:]
                if s_code != '' and s_code not in secret:
                    secret.append(s_code)
                    for x in range(tx, N):
                        for y in range(ty, ty2):
                            arr[x][y] = '0'

    print('# {}'.format(secret))