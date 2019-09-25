def solution(estimates, k):
    N = len(estimates)
    nmax = 0
    for i in range(N-k+1):
        nsum = sum(estimates[i:i+k])
        if nsum > nmax:
            nmax = nsum

    print(nmax)

estimates = [1, 1, 5, 1, 1]
k = 1
solution(estimates, k)