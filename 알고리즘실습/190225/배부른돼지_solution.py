import sys
sys.stdin = open('배부른돼지.txt')

N = int(input())
Ymin = 10
Nmax = 2

for i in range(N):
    cnt, yn = input().split()
    if yn is 'Y':
        if Ymin > int(cnt):
            Ymin = int(cnt)
    else:
        if Nmax < int(cnt):
            Nmax = int(cnt)

if Ymin < Nmax:
    print('F')
else:
    print(Ymin)