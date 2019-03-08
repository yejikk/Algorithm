import sys
sys.stdin = open('스도쿠검증.txt')

def rowcol(arr): # 행, 열탐색
    global N
    flag = 1
    for i in range(N):
        rownum = [] # 행 list
        colnum = [] # 열 list
        for j in range(N):
            # 중복 숫자 검색을 위해서 없으면 append
            if arr[i][j] not in rownum and arr[j][i] not in colnum:
                rownum.append(arr[i][j])
                colnum.append(arr[j][i])
            else:
            # 만약 중복 숫자가 있으면 스도쿠가 아니므로 flag = 0하고 break
                flag = 0
                break
        if not flag:
            break
    return flag

def square(arr):
    # 사각형 탐색
    # 브루트포스 방법 사용해서 풀었어요~
    # 위랑 똑같이 중복된 거 나오면 break
    global N
    flag = 1
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            squarenum = []
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if arr[x][y] not in squarenum:
                        squarenum.append(arr[x][y])
                    else:
                        flag = 0
                        break
                if not flag:
                    break
            if not flag:
                break
        if not flag:
            break

    return flag

test = int(input())

for tc in range(1, test+1):
    N = 9
    arr = [[0]*N for _ in range(N)]
    for k in range(N):
        arr[k] = list(map(int, input().split()))

    # 행, 열, 사각형 전부 중복된 것이 없으면 1 있으면 0
    if rowcol(arr) and square(arr):
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
