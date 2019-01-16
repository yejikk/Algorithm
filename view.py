# max, min method 사용 하지말기!
import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    window = 0
    for i in range(2, N-2):
        if data[i] > data[i-1] and data[i] > data[i-2] and data[i] > data[i+1] and data[i] > data[i+2]:
            left1 = data[i] - data[i-1]
            left2 = data[i] - data[i-2]
            if left1 >= left2:
                left = left2
            elif left1 < left2:
                left = left1
            right1 = data[i] - data[i+1]
            right2 = data[i] - data[i+2]
            if right1 >= right2:
                right = right2
            elif right1 <= right2:
                right = right1

            if left >= right:
                window += right
            else:
                window += left
    print(window)