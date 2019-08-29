import sys
sys.stdin=open("workshop.txt")

T = int(input())
for tc in range(T):
    n = int(input())
    nuts = list(map(int, input().split()))

    cnt = 0
    nut = [[0] * 2 for _ in range(len(nuts) // 2)]
    nutArr = [[0] * 2 for _ in range(len(nuts) // 2)]
    m = 0

    for i in range(len(nuts) // 2):
        for j in range(2):
            nut[i][j] = nuts[m]
            m += 1

    for i in range(len(nut)):
        cnt = 0
        for j in range(len(nut)):
            if nut[i][0] == nut[j][1]:
                {}
            else:
                cnt += 1
        if cnt == (len(nut)):
            nutArr[0] = nut[i]

    for i in range(0, len(nut) - 1):
        for j in range(len(nut)):
            if nutArr[i][1] == nut[j][0]:
                nutArr[i + 1] = nut[j]

    print('#{}'.format(tc + 1), end=' ')
    for i in range(len(nutArr)):
        for j in range(len(nutArr[i])):
            print(nutArr[i][j], end=' ')
    print()