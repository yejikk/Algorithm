import sys
sys.stdin = open('workshop.txt')

for tc in range(1, 11):
    l = int(input())
    t = [list(map(int, input().split())) for i in range(100)]
    cnt = 0
    a = [0] * 100
    for i in range(100):
        for j in range(100):
            if (a[j] == 0 and t[i][j] == 1):
                a[j] = 1
            elif (a[j] == 1 and t[i][j] == 2):
                cnt += 1
                a[j] = 2
            elif (a[j] == 2 and t[i][j] == 1):
                a[j] = 1
    print(f'# {tc} {cnt}')










    # for i in range(N):
    #     mag = []
    #     for j in range(N):
    #         if mag == []:
    #             if arr[j][i] == 1:
    #                 mag.append(arr[j][i])
    #
    #         else:
    #             if j == N-1 and arr[j][i] == 1:
    #                 continue
    #             elif arr[j][i] != 0:
    #                 if mag[-1] != arr[j][i]:
    #                     mag.append(arr[j][i])
    #                     cnt += 1
    #
    # print(f'#{tc} {cnt}')
