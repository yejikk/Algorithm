import sys
sys.stdin = open('책꽂이.txt')

def dfs(no, nsum):
    global num_min

    if nsum > num_min:
        return

    if no >= N:
        if nsum >= B and nsum < num_min:
            num_min = nsum
        return

    temp[no] = height[no]
    dfs(no+1, nsum+temp[no])
    temp[no] = 0
    dfs(no+1, nsum)

T = int(input())

for tc in range(T):
    N, B = map(int, input().split())
    height = [0] * N
    temp = [0] * N

    for i in range(N):
        height[i] = int(input())

    num_min = 9999999999
    dfs(0, 0)
    print(num_min - B)