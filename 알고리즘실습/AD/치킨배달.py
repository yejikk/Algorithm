import sys
sys.stdin = open('치킨배달.txt')

def distance(chk):
    cnt = 0
    for i in range(len(home)):
        nmin = 10000000
        for j in range(len(store)):
            if chk[j]:
                if temp[j][i] < nmin:
                    nmin = temp[j][i]
        cnt += nmin

    return cnt

def dfs(no, cnt):
    global M, sol
    if cnt == M:
        # print(chk)
        total = distance(chk)
        if total < sol:
            sol = total
        return

    if no >= len(chk):
        return

    chk[no] = 1
    dfs(no+1, cnt+1)
    chk[no] = 0
    dfs(no+1, cnt)

N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for n in range(N):
    arr[n] = list(map(int, input().split()))

home = []
store = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            store.append([i, j])

temp = [[0]* len(home) for _ in range(len(store))]

for i in range(len(store)):
    for j in range(len(home)):
        di = abs(store[i][0] - home[j][0]) + abs(store[i][1] - home[j][1])
        temp[i][j] = di
    # print(temp[i])

sol = 1000000000
chk = [0]*len(store)
dfs(0, 0)
print(sol)