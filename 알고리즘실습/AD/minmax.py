import sys
sys.stdin = open('minmax.txt')

def max_num(numbers):
    num_max = 0
    for num in numbers:
        if num > num_max:
            num_max = num

    return num_max

def min_num(numbers):
    num_min = 99999999
    for num in numbers:
        if num < num_min:
            num_min = num

    return num_min

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    num1 = max_num(numbers)
    num2 = min_num(numbers)

    print('#{} {}'.format(tc, num1-num2))