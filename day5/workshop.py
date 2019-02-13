import sys
sys.stdin = open('workshop.txt')

def two(arr):
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                x = i
                y = j
                return x, y

for tc in range(10):
    case = input()
    arr = [[0]*100 for _ in range(100)]

    for i in range(100):
        arr[i] = list(map(int, input().split()))

    x, y = two(arr)
    x = x-1

    while x > 0:
        if arr[x][y-1] == 0 and arr[x][y+1] == 0:
            x -= 1

        elif arr[x][y-1] == 1 and arr[x][y+1] == 0:
            y -= 1

        elif arr[x][y-1] == 0 and arr[x][y+1] == 1:
            y += 1

        elif arr[x][y - 1] == 1 and arr[x][y + 1] == 1:



    print(f'#{case} {x} {y}')


