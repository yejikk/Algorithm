import sys
sys.stdin = open('최소의합.txt')

def DFS(no, nsum):
    global nmin
    # if nsum > nmin:
    #     return

    if no == N:
        for i in range(N):
            print(rec[i], end=' ')
        print()
        if nsum < nmin:
            nmin = nsum
        return

    for i in range(N):
        rec[no] = arr[no][i]
        DFS(no+1, nsum + arr[no][i])

def DFS2(no, nsum):
    global nmin
    if no == N:
        for i in range(N):
            print(rec[i], end=' ')
        print()
        if nsum < nmin:
            nmin = nsum
        return

    for i in range(N):
        if chk[i] == 1:
            continue
        chk[i] = 1
        rec[no] = arr[no][i]
        DFS2(no+1, nsum + arr[no][i])
        chk[i] = 0

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

nmin = 10000000
rec = [0] * N
DFS(0, 0)
print('중복허용:', nmin)

print('--------------')

nmin = 10000000
rec = [0] * N
chk = [0] * N
DFS2(0, 0)
print('중복배제:', nmin)