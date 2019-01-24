import sys
sys.stdin = open("부분집합의 합.txt")

def arrset(arr):
    n = len(arr)
    subset = [[] for _ in range(2**n)]
    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
                subset[i].append(arr[j])
    return subset

test = int(input())
arr = list(range(1, 13))
subset = arrset(arr)

for tc in range(1, test+1):
    data, sums = map(int, input().split())
    cnt = 0
    for i in range(len(subset)):
        if len(subset[i]) == data and sum(subset[i]) == sums:
            cnt += 1
    print(f'#{tc} {cnt}')
