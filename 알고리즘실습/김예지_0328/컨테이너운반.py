import sys
sys.stdin = open('컨테이너운반.txt')

def Nsort(arr, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
test = int(input())

for tc in range(1, test+1):
    N, M = map(int, input().split())
    cont = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    Nsort(cont, N)
    Nsort(truck, M)
    sol = 0

    for i in range(N):
        for j in range(M):
            if cont[i] <= truck[j]:
                sol += cont[i]
                truck[j] = 0
                break
    print('#{} {}'.format(tc, sol))