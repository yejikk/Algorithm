import sys
sys.stdin = open('화물도크.txt')

def Nsort():
    for i in range(N-1):
        for j in range(i+1, N):
            if work[j][0] < work[i][0]:
                work[i], work[j] = work[j], work[i]
            elif work[i][0] == work[j][0]:
                if work[j][1] < work[i][1]:
                    work[i], work[j] = work[j], work[i]

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    work = []
    for i in range(N):
        work.append(list(map(int, input().split())))
    Nsort()
    dock = []
    # print(work)
    cnt = 1
    s = 0
    e = 0
    for i in range(N):
        if not dock:
            dock.append(work[i])
        else:
            v = dock[-1]
            if v[0] != work[i][0]:
                if v[0] < work[i][0] and v[1] > work[i][1]:
                    dock.pop()
                    dock.append(work[i])
                elif v[1] <= work[i][0]:
                    dock.append(work[i])
                    cnt += 1
    print('#{} {}'.format(tc, cnt))
