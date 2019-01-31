import sys
sys.stdin = open("회문_input.txt")

test = int(input())

def arreverse(arry):
    newarr = arry[:]
    for i in range(len(arry)//2):
        x = newarr[i]
        newarr[i] = newarr[len(newarr)-1-i]
        newarr[len(newarr)-1-i] = x
    if newarr == arry:
        return arry

for tc in range(1, test+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    for i in range(N):
        arr[i] = list(input())

    for i in range(N):
        rowarr = arr[i][:]
        for j in range(N-M+1):
            old = rowarr[j:M+j][:]
            newarr = arreverse(old)
            if newarr:
                result = old
                break

    if bool(result) == False:
        for j in range(N):
            colarr = []
            for i in range(N):
                colarr.append(arr[i][j])
            for k in range(N-M+1):
                old = colarr[k:M+k][:]
                newarr = arreverse(old)
                if newarr:
                    result = old
                    break

    result = ''.join(result)
    print(f'#{tc} {result}')