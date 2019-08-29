import sys
sys.stdin = open('workshop2.txt')

def comb(n, k, nsum):
    global N, nmin, B
    if nsum > nmin:
        return
    if n == k:
        if B <= nsum < nmin:
            nmin = nsum
    else:
        temp[k] = 1
        comb(n, k+1, nsum + height[k])
        temp[k] = 0
        comb(n, k+1, nsum)

test = int(input())

for tc in range(1, test+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    temp = [0 for _ in range(N)]
    nmin = 999999999999
    comb(N, 0, 0)
    print('#{} {}'.format(tc, nmin - B))


