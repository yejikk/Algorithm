import sys
sys.stdin = open("learn_회문.txt")

test = int(input())

def arreverse(colarr):
    if colarr == colarr[::-1]:
        return True
    else:
        return False

def brute(colarr, M, N):
    for j in range(N-M+1):
        if colarr[j:M+j] == colarr[j:M+j][::-1]:
            return colarr[j:M+j]

for tc in range(1, test+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    for i in range(N):
        arr[i] = list(input())

    if N == M:
        for i in range(N):
            if arr[i] == arr[i][::-1]:
                result = arr[i]
                break

        if result == []:
            for j in range(N):
                colarr = []
                for i in range(N):
                    colarr.append(arr[i][j])
                result = arreverse(colarr)
                if result:
                    result = colarr
                    break
    else:
        for i in range(N):
            result = brute(arr[i], M, N)
            if result:
                    break

        if bool(result) == False:
            for j in range(N):
                colarr = []
                for i in range(N):
                    colarr.append(arr[i][j])
                result = brute(colarr, M, N)
                if result:
                    break

    result = ''.join(result)
    print(f'#{tc} {result}')