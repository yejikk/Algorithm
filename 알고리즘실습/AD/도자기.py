import sys
sys.stdin = open('도자기.txt')

def dfs(no):
    if no == N:
        if chk.count(1) == M:
            temp = []
            for i in range(N):
                if chk[i] == 1:
                    temp.append(data[i])

            if sorted(temp) not in result:
                result.append(sorted(temp))
        return

    chk[no] = 1
    dfs(no+1)

    chk[no] = 0
    dfs(no+1)

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    chk = [0] * N

    result = []
    dfs(0)
    print(len(result))