import sys
sys.stdin = open('기업투자.txt')

def perm(no, nsum):
    global nmax, M, N, chk, cn

    if no >= N:
        if nmax < nsum:
            nmax = nsum
        return

    for i in range(1, N+1):
        if chk[i]:
            continue
        chk[i] = 1
        perm(no+1, nsum+cn[no][i])
        chk[i] = 0

def comb(n, r):
    global M, N
    if r == 0:
        num = 0
        for i in range(N):
            num += cn[i][0]
        if num == M:
            perm(0, 0)
        return

    elif n == 0:
        return

    else:
        cn[r-1] = temp[n-1]
        comb(n, r-1)
        comb(n-1, r)

M, N = map(int, input().split())

temp = [[0] * (N+1)]
for _ in range(M):
    temp.append(list(map(int, input().split())))

nmax = 0
done = list(map(int, range(M+1)))
chk = [0] * (N+1)
cn = [0] * N
comb(M+1, N)
print(nmax)