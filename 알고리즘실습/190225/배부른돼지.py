import sys
sys.stdin = open('배부른돼지.txt')

count = int(input())
arr = [[0]*count for _ in range(count)]
for i in range(count):
    arr[i] = list(input().split())

cntmin = 101
flag = 0

if count == 0:
    flag = 1

for i in range(count):
    if int(arr[i][0]) > 2 and int(arr[i][0]) < 10:
        if arr[i][1] == 'Y':
            if int(arr[i][0]) < cntmin:
                cntmin = int(arr[i][0])

        else:
            if int(arr[i][0]) > cntmin:
                flag = 1
    if flag:
        break

if flag:
    print('F')
else:
    print(cntmin)