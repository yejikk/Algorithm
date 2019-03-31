import sys
sys.stdin = open('테이프이어붙이기.txt')

def powerset(n, k):
    global nmin
    if n == k:
        sol1 = 0
        sol2 = 0
        if sum(temp) == (N//2):
            for i in range(N):
                if temp[i] == 1:
                    sol1 += tape[i]

                else:
                    sol2 += tape[i]
            total = abs(sol1 - sol2)
            if total < nmin:
                nmin = total

    else:
        temp[k] = 1
        powerset(n, k+1)
        temp[k] = 0
        powerset(n, k+1)

N = int(input())
tape = list(map(int, input().split()))
temp = [0] * N
nmin = 10000000
powerset(N, 0)
print(nmin)

