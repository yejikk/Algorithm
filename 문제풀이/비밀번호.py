import sys
sys.stdin = open('비밀번호.txt')

for tc in range(1, 11):
    N, number = map(str, input().split())
    number = list(map(int, number))
<<<<<<< HEAD

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
=======
    while True:
        check = 0
        for i in range(len(number)-1):
            if number[i] == number[i+1]:
                number.remove(number[i+1])
                number.remove(number[i])
                check += 1
                break
        if check == 0:
            break
    print(number)
>>>>>>> 3946bfc9ead3be0cbaf05d3b8d507eb04e90145d
