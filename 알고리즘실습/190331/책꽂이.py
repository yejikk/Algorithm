import sys
sys.stdin = open('책꽂이.txt')

def powerset(n, k, nsum):
    global nmin
    if nsum > nmin:
        return

    if n == k:
        cnt = 0
        for i in range(N):
            if temp[i] == 1:
                cnt += height[i]
        if B <= cnt < nmin:
            nmin = cnt

    else:
        temp[k] = 1
        powerset(n, k+1, nsum + height[k])
        temp[k] = 0
        powerset(n, k+1, nsum)


test = int(input())

for tc in range(test):
    N, B = map(int, input().split())
    temp = [0] * N
    height = []
    for _ in range(N):
        height.append(int(input()))

    nmin = 10000000
    powerset(N, 0, 0)
    print(nmin - B)