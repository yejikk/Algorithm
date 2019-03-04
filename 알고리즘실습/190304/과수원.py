# i, j for문 안에서 똑같이 써주지 말기 마지막 i랑 j가 저장되어서 index 이상해짐
import sys
sys.stdin = open('과수원.txt')

def count(arr, i, j):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    for x in range(i+1):
        for y in range(j+1):
            if arr[x][y] == 1:
                cnt1 += 1

    for x in range(i+1):
        for y in range(j+1, N):
            if arr[x][y] == 1:
                cnt2 += 1

    for y in range(j+1):
        for x in range(i+1, N):
            if arr[x][y] == 1:
                cnt3 += 1

    for x in range(i+1, N):
        for y in range(j+1, N):
            if arr[x][y] == 1:
                cnt4 += 1

    if cnt1 == cnt2 == cnt3 == cnt4:
        return True
    else:
        return False

N = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

cnt = 0
for i in range(N):
    for j in range(N):
        if count(arr, i, j):
            cnt += 1

if cnt:
    print(cnt)
else:
    print(-1)
