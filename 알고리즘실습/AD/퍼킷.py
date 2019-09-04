import sys
sys.stdin = open('퍼킷.txt')

def dfs(no, smul, bsum):
    global nmin

    if no >= N:
        if sum(t1) == N:
            if bsum != 0:
                if nmin > abs(smul - bsum):
                    nmin = abs(smul - bsum)
        else:
            if smul != 1 and bsum != 0:
                if nmin > abs(smul - bsum):
                    nmin = abs(smul - bsum)
        return

    dfs(no+1, smul*t1[no], bsum+t2[no])
    dfs(no+1, smul, bsum)

N = int(input())

t1 = [0] * N

t2 = [0] * N

for i in range(N):
    x, y = map(int, input().split())
    # 신맛
    t1[i] = x
    # 쓴맛
    t2[i] = y

nmin = 99999999
dfs(0, 1, 0)
print(nmin)