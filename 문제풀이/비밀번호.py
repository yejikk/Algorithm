import sys
sys.stdin = open('비밀번호.txt')

for tc in range(1, 11):
    N, number = map(str, input().split())
    number = list(map(int, number))
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