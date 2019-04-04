import sys
sys.stdin = open('더하기.txt')

def DFS(no, nsum):
    global flag
    if nsum > K:
        return

    if nsum == K:
        flag = 1
        return

    if no == N:
        # for i in range(N):
        #     print(temp[i], end=' ')
        # print()
        # if nsum == K:
        #     flag = 1
        return

    # temp[no] = arr[no]
    DFS(no+1, nsum + arr[no])
    # temp[no] = 0
    DFS(no+1, nsum)

test = int(input())

for tc in range(test):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    temp = [0] * N
    flag = 0
    DFS(0, 0)
    if flag:
        print('YES')
    else:
        print('NO')