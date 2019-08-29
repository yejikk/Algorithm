import sys
sys.stdin = open('workshop.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        mag = []
        for j in range(N):
            if mag == []:
                if arr[j][i] == 1:
                    mag.append(1)
            else:
                if arr[j][i] != 0:
                    if mag[-1] != arr[j][i]:
                        mag.append(arr[j][i])
                        if mag[-1] == 2:
                            cnt += 1

    print(f'#{tc} {cnt}')