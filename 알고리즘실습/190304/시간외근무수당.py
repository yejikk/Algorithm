import sys
sys.stdin = open('시간외근무수당.txt')

work = [[0]*2 for _ in range(5)]
for i in range(5):
    work[i] = list(map(float, input().split()))

time = 0

for i in range(5):
    timeout = work[i][1]-work[i][0]-1
    if timeout > 0 and timeout < 4:
        time += timeout
    elif timeout >= 4:
        time += 4

money = time * 10000
if time <= 5:
    worksum = money * 0.05
    money += worksum
elif time >= 15:
    worksum = money * 0.05
    money -= worksum

print(int(money))