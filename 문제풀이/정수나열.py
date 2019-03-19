import sys
sys.stdin = open('정수나열.txt')

test = int(input())

# 이어지는 것들은 다 숫자가 되기 때문에 안에 있기만 하면됨..
# 나중에 다시 풀어보기
for tc in range(1, test+1):
    N = int(input())
    num = []
    result = 0
    while len(num) != N:
        num.extend(input().split())

    num = ''.join(num)

    while str(result) in num:
        result += 1

    print('#{} {}'.format(tc, result))