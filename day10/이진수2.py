import sys
sys.stdin = open('이진수2.txt')

test = int(input())

for tc in range(1, test+1):
    number = float(input())
    result = ''
    while True:
        number = number * 2
        if number > 1.0:
            number = number - 1
            result += '1'

        elif number < 1.0:
            result += '0'

        elif number == 1.0:
            result += '1'
            break

    if len(result) >= 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')