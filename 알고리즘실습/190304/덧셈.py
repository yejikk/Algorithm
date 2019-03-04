# num[:0]은 아무것도 출력되지않고, int형으로도 바꿀 수 없다. 그래서 n+1부터 시작
import sys
sys.stdin = open('덧셈.txt')

num, sums = map(str, input().split())
sums = int(sums)
i = 0
flag = 0
while True:
    SA = int(num[:i+1])
    SB = int(num[i+1:])
    numsum = SA + SB
    if numsum == sums:
        print(str(SA)+'+'+str(SB)+'='+str(numsum))
        break
    i += 1
    if i >= len(num)-1:
        flag = 1
        break

if flag:
    print('NONE')