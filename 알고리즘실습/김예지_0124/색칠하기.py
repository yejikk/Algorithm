import sys
sys.stdin = open("색칠하기.txt")

test = int(input())

for tc in range(1, test+1):
    arr = [[0 for _ in range(10)] for _ in range(10)]
    num = int(input())
    colorlist = [[0 for _ in range(5)] for _ in range(num)]
    for n in range(num):
        colorlist[n] = list(map(int, input().split()))

    cnt = 0

    for i in range(len(colorlist)):
        r1 = colorlist[i][0]
        c1 = colorlist[i][1]
        r2 = colorlist[i][2]
        c2 = colorlist[i][3]
        color = colorlist[i][4]
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                arr[x][y] += color

    for k in range(len(arr)):
        for l in range(len(arr)):
            if arr[k][l] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')