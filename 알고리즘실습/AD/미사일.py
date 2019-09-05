import sys
sys.stdin = open('미사일.txt')

def shoot():
    global N, M, fire, scope
    for i in range(M):
        if cn[i][2] > 0:
            cn[i][2] -= fire
            for j in range(N):
                if cn[i] != temp[j] and temp[j][2] > 0:
                    if abs(cn[i][0] - temp[j][0]) + abs(cn[i][1] - temp[j][1]) <= scope:
                        temp[j][2] -= fire
    return

def stay():
    cnt = 0
    for i in range(N):
        if temp[i][2] > 0:
           cnt += 1
    return cnt

def comb(n, r):
    global N, copy, nmin
    if r == 0:
        shoot()
        cnt = stay()
        if cnt < nmin:
            nmin = cnt

        for i in range(N):
            temp[i][2] = copy[i]
        return

    elif n < r:
        return

    else:
        cn[r-1] = temp[n-1]
        comb(n, r-1)
        comb(n-1, r)

N = int(input())
temp = []

for i in range(N):
    v = list(map(int, input().split()))
    temp.append(v)

M, fire, scope = map(int, input().split())

# 뽑아야하는 갯수
cn = [0] * M

# copy
copy = [0] * N
for i in range(N):
    copy[i] = temp[i][2]

nmin = 1000000000
comb(N, M)
print(nmin)