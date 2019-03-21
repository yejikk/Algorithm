import sys
sys.stdin = open('정식이의은행업무.txt')

def change(number):
    m = 0
    for l in range(len(number)):
        m = m * 3 + number[l]
    return m

test = int(input())

for tc in range(1, test+1):
    B = list(map(int, input()))
    T = list(map(int, input()))
    b_num = []
    t_num = []
    for i in range(len(B)):
        binary = B[:]
        n = 0
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0
        for j in range(len(B)):
            n = n * 2 + binary[j]
        b_num.append(n)

    for j in range(len(T)):
        thine = T[:]
        m = 0
        if thine[j] == 0:
            thine[j] = 1
            t_num.append(change(thine))
            thine[j] = 2
            t_num.append(change(thine))

        elif thine[j] == 1:
            thine[j] = 0
            t_num.append(change(thine))
            thine[j] = 2
            t_num.append(change(thine))

        elif thine[j] == 2:
            thine[j] = 0
            t_num.append(change(thine))
            thine[j] = 1
            t_num.append(change(thine))

    flag = 0
    for x in b_num:
        for y in t_num:
            if x == y:
                flag = 1
                print('#{} {}'.format(tc, x))
                break
        if flag:
            break