import sys, pprint
sys.stdin = open('workshopp.txt')

def find(binary):
    global N, M
    change = []
    for i in range(len(binary)):
        q = len(binary[i]) // 56
        num = [[] for _ in range(8)]
        idx = 0
        binary[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + binary[i]
        for j in range(len(binary[i])-1, -1, -1):
            if binary[i][j] == 1:
                yidx = j
                break
        binary[i] = binary[i][:yidx+1]
        binary[i] = binary[i][::-1]
        # print(yidx)
        for k in range(0, len(binary[i]), (7*q)):
            b = binary[i][k:k+(7*q)]
            # print(b)
            if b[0] == 1:
                flag = 1
            else:
                flag = 0
            zero_cnt = 0
            one_cnt = 0
            for n in range(len(b)):
                if flag == 0 and b[n] == 0:
                    zero_cnt += 1

                elif flag == 0 and b[n] == 1:
                    flag = 1
                    num[idx].append(zero_cnt)
                    zero_cnt = 0
                    one_cnt += 1

                elif flag == 1 and b[n] == 1:
                    one_cnt += 1

                elif flag == 1 and b[n] == 0:
                    flag = 0
                    num[idx].append(one_cnt)
                    one_cnt = 0
                    zero_cnt += 1
            if zero_cnt != 0:
                num[idx].append(zero_cnt)
            if one_cnt != 0:
                num[idx].append(one_cnt)
            idx += 1
            # print(num)
            if idx == 8:
                change.append(num)
                break

        # for j in range(len(binary[i])-1, -1, -(7*q)):
        #     if j-(7*q)+1 < 0:
        #         break
        #     else:
        #         b = binary[i][j-(7*q)+1:j+1]
        #         print(b)
        #         print(len(b))
        #         if b[0] == 1:
        #             flag = 1
        #         else:
        #             flag = 0
        #         zero_cnt = 0
        #         one_cnt = 0
        #         for n in range(len(b)):
        #             if flag == 0 and b[n] == 0:
        #                 zero_cnt += 1
        #
        #             elif flag == 0 and b[n] == 1:
        #                 flag = 1
        #                 num[idx].append(zero_cnt)
        #                 zero_cnt = 0
        #                 one_cnt += 1
        #
        #             elif flag == 1 and b[n] == 1:
        #                 one_cnt += 1
        #
        #             elif flag == 1 and b[n] == 0:
        #                 flag = 0
        #                 num[idx].append(one_cnt)
        #                 one_cnt = 0
        #                 zero_cnt += 1
        #         if zero_cnt != 0:
        #             num[idx].append(zero_cnt)
        #         elif one_cnt != 0:
        #             num[idx].append(one_cnt)
        #         idx += 1
        #         print(num)
        #         if idx == 8:
        #             change.append(num)
        #             break
        #     print(num)
    # pprint.pprint(change)
    # print(len(change))
    return num

def aToh(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def makeT(idx, x):
    global binary, asc
    for i in range(4):
        binary[idx].append(asc[x][i])

test = int(input())

for tc in range(1, test+1):
    asc = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1],
           [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
           [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
           [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]

    code = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2],
            [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1],
            [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3],
            [3, 1, 1, 2]]

    N, M = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for i in range(N):
        arr[i] = list(input())

    ix = 0
    secret = []
    for i in range(ix, N):
        s_code = []
        flag = 0
        for j in range(M-1, -1, -1):
            s_code = []
            if arr[i][j] != '0' and arr[i-1][j] == '0':
                ty2 = j
                for k in range(ty2, -1, -1):
                    flag = 1
                    s_code.append(arr[i][k])

                s_flag = 0
                s_code = s_code[::-1]
                print('p',s_code)
                if s_code[0] == '0':
                    while True:
                        for s in range(len(s_code)):
                            if s_code[s] != '0':
                                s_code = s_code[s:]
                                s_flag = 1
                                break
                        if s_flag:
                            break
                print('after', s_code)
                if s_code not in secret:
                    secret.append(s_code)
            if flag:
                # ix += 1
                break
        print(i, secret)
        '''
        for j in range(M-1, -1, -1):
            s_code = []
            if arr[i][j] != '0' and arr[i-1][j] == '0':
                ty2 = j
                for k in range(ty2, -1, -1):
                    flag = 1
                    s_code.append(arr[i][k])

                s_flag = 0
                s_code = s_code[::-1]
                if s_code[0] == '0':
                    while True:
                        for s in range(len(s_code)):
                            if s_code[s] != '0':
                                s_code = s_code[s:]
                                s_flag = 1
                                break
                        if s_flag:
                            break

                if s_code not in secret:
                    secret.append(s_code)
            if flag:
                # ix += 1
                break
        print(i, s_code)
        '''
    binary = [[] for _ in range(len(secret))]
    for x in range(len(secret)):
        for y in range(len(secret[x])):
            makeT(x, aToh(secret[x][y]))
        # print(binary)

    find(binary)
    # for o in range(len(secret)):
    #     print(len(secret[o]))
    #     print(secret[o])
    # print(binary)
    # for l in range(len(binary)):
    #     print(len(binary[l]))
    #     print(binary[l])

    # print(len(binary))
    # print(binary)
    print('#{} {} {}'.format(tc, N, M))
    print('#{} {} {}'.format(tc, len(secret), len(binary)))
    print()
    # print('#{} {}'.format(tc, secret))
