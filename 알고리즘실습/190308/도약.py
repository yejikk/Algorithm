import sys
sys.stdin = open('도약.txt')

N = int(input())
leaf = []
for i in range(N):
    leaf.append(int(input()))
leaf.sort()

cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        jump = leaf[j] - leaf[i]
        for k in range(j+1, N):
            if jump <= (leaf[k] - leaf[j]) <= (jump*2):
                cnt += 1
print(cnt)