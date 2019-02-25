import sys
sys.stdin = open('숫자맞추기.txt')

N = int(input())
arr = [[0]*N for _ in range(N)]
result = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(3): # 게임 몇판?(생각해줘야함) 세번...
    for j in range(N): # 플레이어 수
        flag = 0
        score = arr[j][i]
        for k in range(N):
            if j == k:
                continue
            else:
                if arr[k][i] == score:
                    flag = 1
                    break
                else:
                    flag = 0
                    continue
        if flag:
            result[j] += 0
        else:
            result[j] += score

for i in range(len(result)):
    print(result[i])