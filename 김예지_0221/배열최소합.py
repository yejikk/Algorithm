import sys
sys.stdin = open('배열최소합.txt')

test = int(input())

def process(a, k, arrsum):
    global arrmin
    if arrsum > arrmin:
        return

def make_candidates(a, k, N, c):
    in_perm = [0] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = 1

    ncands = 0
    for i in range(1, N+1):
        if in_perm[i] == 0:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, N, arrsum):
    global MAXCANDIDATES, arrmin
    c = [0] * MAXCANDIDATES

    if arrsum > arrmin:
        return

    if k == N:
        process(a, k, arrsum)
        if arrmin > arrsum:
            arrmin = arrsum
    else:
        k += 1
        ncands = make_candidates(a, k, N, c)

        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, N, arrsum + arr[k-1][a[k]-1])

for tc in range(1, test+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    arrmin = 99999
    MAXCANDIDATES = 100
    NMAX = 100
    data = [0] + list(map(int, range(N)))
    a = [0] * NMAX
    backtrack(a, 0, N, 0)
    print(f'#{tc} {arrmin}')