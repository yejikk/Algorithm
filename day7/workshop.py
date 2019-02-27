import sys
sys.stdin = open('workshop.txt')

def index(arr):
    flag = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                x = i
                y = j
                flag = 1
                return x, y
                break
        if flag:
            break
    return -1, -1

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    size = []
    while arr:
        row = 0
        col = 0
        rowcnt = []
        colcnt = []
        x, y = index(arr)
        if x == -1 and y == -1:
            break
        else:
            for i in range(x, N):
                flag = 0
                col = 0
                for j in range(y, N):
                    if arr[i][j] != 0:
                        col += 1
                        continue
                    else:
                        if arr[i][y] == 0 and arr[i][j] == 0:
                            colcnt.append(col)
                            flag = 1
                            break
                        else:
                            break

                if flag:
                    break
                else:
                    row += 1
                    colcnt.append(col)

            if row != 0:
                rowcnt.append(row)

        if rowcnt and colcnt:
            row = rowcnt[0]
            col = colcnt[0]
            size.append([row*col, row, col])

            for i in range(x, x+row):
                for j in range(y, y+col):
                    arr[i][j] = 0

    size.sort()
    print(f'#{tc} {len(size)}', end = ' ')
    for i in range(len(size)):
        result = size[i][1:]
        print(' '.join(map(str, result)), end=' ')
    print()
    # print(len(size))
    # print(size)

