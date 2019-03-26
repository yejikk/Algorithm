import sys
sys.stdin = open('예산.txt')

N = int(input())
budget = list(map(int, input().split()))
limit = int(input())

budget.sort()

s = 0
e = budget[-1]
maxnum = 0
maxsum = 0

while s <= e:
    sums = 0
    mid = (s + e) // 2

    for i in range(N):
        if budget[i] > mid:
            sums += mid

        else:
            sums += budget[i]

    if sums >= limit:
        e = mid - 1

    elif sums < limit:
        s = mid + 1

    if sums > maxnum and sums <= limit:
        maxsum = sums
        maxnum = mid

print(maxnum)