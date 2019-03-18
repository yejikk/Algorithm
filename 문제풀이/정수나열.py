import sys
sys.stdin = open('정수나열.txt')

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    number =
    num = []
    length = 0
    while length != N:
        num.append(list(map(int, input().split())))
        length += len(num[-1])

    for i in range(len(num)):
        for j in range(len(num[i])):
