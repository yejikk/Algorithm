import sys
sys.stdin = open('건물세우기.txt')

def perm(n, nsum):
    global nmin
    if nsum > nmin:
        return

    if n >= N:
        if nsum < nmin:
            nmin = nsum
    else:
        for i in range(N):
            if chk[i] == 1:
                continue
            chk[i] = 1
            perm(n+1, nsum+arr[n][i])
            chk[i] = 0

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

chk = [0] * N
nmin = 10000000
perm(0, 0)
print(nmin)