def solution(office, k):
    N = len(office)
    nmax = 0

    for i in range(N-k+1):
        for j in range(N-k+1):
            nsum = 0
            for x in range(i, i+k):
                for y in range(j, j+k):
                    nsum += office[x][y]

            if nsum > nmax:
                nmax = nsum

    print(nmax)

office = [[1,0,0],[0,0,1],[1,0,0]]
k = 2
solution(office, k)