import sys
sys.stdin = open('월동준비.txt')

N = int(input())
number = list(map(int, input().split()))

smart = 0
mins = -10000000000
for i in range(N):
    if number[i] < 0 and number[i] > mins:
        mins = number[i]
    elif number[i] > 0:
        smart += number[i]
if smart == 0:
    smart = mins

notsmart = 0
notsum = -10000000000
for i in range(N):
    if notsmart + number[i] < number[i]:
        notsmart = number[i]
    else:
        notsmart += number[i]
    if notsmart > notsum:
        notsum = notsmart

print(notsum, smart)
