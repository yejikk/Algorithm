import sys
sys.stdin = open("d3-3.txt")

test = int(input())

for tc in range(1, test+1):
    block = int(input())
    height = list(map(int, input().split()))
    high = 0
    low = 0
    for i in range(block-1):
        if height[i] < height[i+1]:
            if height[i+1] - height[i] > high:
                high = height[i+1] - height[i]
        else:
            if height[i] - height[i+1] > low:
                low = height[i] - height[i+1]

    print(f'#{tc} {high} {low}')
