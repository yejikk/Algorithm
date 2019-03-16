import sys
sys.stdin = open('비밀번호.txt')

for tc in range(1, 11):
    N, number = map(str, input().split())
    number = list(map(int, number))

    password = []
    password.append(number[0])
    for i in range(1, int(N)):
        if len(password) != 0:
            if password[-1] == number[i]:
                password.pop()
            else:
                password.append(number[i])
        else:
            password.append(number[i])
    password = ''.join(map(str, password))
    print('#{} {}'.format(tc, password))