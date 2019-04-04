import sys
sys.stdin = open('건물세우기.txt')

def DFS(no, nsum):
    global nmin
    if nsum > nmin:
        return

    if no == N:
        if nsum < nmin:
            nmin = nsum
        return

    for i in range(N):
        if chk[i] == 1:
            continue
        chk[i] = 1
        rec[no] = arr[no][i]
        DFS(no+1, nsum + arr[no][i])
        chk[i] = 0

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
nmin = 10000000
chk = [0]*N
rec = [0]*N
DFS(0, 0)
print(nmin)