import sys
sys.stdin = open('workshop.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    cnt = 0

    for i in range(N):
        check = 0
        for j in range(N):
            if check == 0 and arr[j][i] == 1:
                check = 1
            elif check == 1 and arr[j][i] == 2:
                check = 0
                cnt += 1
    print(f'#{tc} {cnt}')
