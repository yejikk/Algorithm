import sys
sys.stdin = open('건물세우기.txt')

def dfs(no, nsum):
    global num_min
    if nsum > num_min:
        return

    if no >= N:
        if nsum < num_min:
            num_min = nsum

    for i in range(N):
        if chk[i]:
            continue
        chk[i] = 1
        dfs(no+1, nsum+arr[no][i])
        chk[i] = 0

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

chk = [0]*N
num_min = 999999999
dfs(0, 0)
print(num_min)