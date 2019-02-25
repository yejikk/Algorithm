import sys
sys.stdin = open('숫자근.txt')

def root(number):
    while True:
        total = 0
        while number:
            total += (number % 10)
            number //= 10
        total += number
    return total
N = int(input())
maxroot = 0
minnum = 0

for i in range(N):
    number = input()
    number = number.replace(' ', '')

    number = int(number)
    result = root(number)
    print(result)

    if result == maxroot:
        if number < minnum:
            minnum = number
            maxroot = result

    if result > maxroot:
        maxroot = result
        minnum = number

    print(minnum, maxroot)
