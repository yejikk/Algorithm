import sys
sys.stdin = open('숫자근.txt')

def root(number):
    number = list(map(int, number))
    while len(number) != 1:
        numsum = 0
        for n in number:
            numsum += n
        numsum = str(numsum)
        number = list(map(int, numsum))
    return ''.join(map(str, number))

N = int(input())
maxroot = 0
maxnum = 0

for i in range(N):
    number = input()
    number = number.replace(' ', '')
    result = root(number)
    result = int(result)

    if maxroot == result:
        if int(number) < maxnum:
            maxnum = int(number)
            maxroot = result

    elif result > maxroot:
        maxnum = int(number)
        maxroot = result

    print(maxnum, maxroot)
