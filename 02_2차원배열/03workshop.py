import sys
sys.stdin = open("03workshop.txt")

for tc in range(1, 11):
    test = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    arrmax = 0
    linesum1 = 0
    linesum2 = 0

    for i in range(100):
        rowsum = 0
        for j in range(100):
            rowsum += arr[i][j]
            if rowsum > arrmax:
                arrmax = rowsum

    for k in range(100):
        colsum = 0
        for l in range(100):
            colsum += arr[l][k]
            if colsum > arrmax:
                arrmax = colsum

    for x in range(100):
        linesum1 += arr[x][x]
        if linesum1 > arrmax:
            arrmax = linesum1

    for y in range(99, -1, -1):
        linesum2 += arr[y][y]
        if linesum2 > arrmax:
            arrmax = linesum2

    print(f'#{tc} {arrmax}')
