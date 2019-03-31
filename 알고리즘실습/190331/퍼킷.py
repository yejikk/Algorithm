import sys
sys.stdin = open('퍼킷.txt')

def powerset(n, k):
    global nmin
    if n == k:
        smul = 1
        bsum = 0
        for i in range(N):
            if temp[i] == 1:
                smul *= food[i][0]
                bsum += food[i][1]
        if smul != 1 and bsum != 0:
            total = smul - bsum
            total = abs(total)
            if 0 <= total < nmin:
                nmin = total

    else:
        temp[k] = 1
        powerset(n, k+1)
        temp[k] = 0
        powerset(n, k+1)

N = int(input())
food = []
temp = [0]*N
for _ in range(N):
    food.append(list(map(int, input().split())))
nmin = 10000000
powerset(N, 0)
print(nmin)

