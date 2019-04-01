import sys
sys.stdin = open('양팔저울.txt')

# 1. 왼쪽에 올리는 경우
# 2. 오른쪽에 올리는 경우
# 3. 모두 사용하지 않는 경우
# 3중 재귀를 사용해야함

def DFS(no, Lsum, Rsum):
    global sol
    if sol: # 가지치기
        return

    if no >= CN:
        for i in range(CN):
            print(rec[i], end=' ')
        print(Lsum, Rsum)
        if Lsum == Rsum:
            sol = 1
        return

    # 현재 추를 왼쪽에 올려보기
    rec[no] = chu[no]
    DFS(no+1, Lsum+chu[no], Rsum)

    # 현재 추를 오른쪽에 올려보기
    rec[no] = -chu[no]
    DFS(no+1, Lsum, Rsum+chu[no])

    # 현재 추를 사용하지 않기
    rec[no] = 0
    DFS(no+1, Lsum, Rsum)

CN = int(input())
chu = list(map(int, input().split()))
BN = int(input())
ball = list(map(int, input().split()))
rec = [0] * CN # 기록

for i in range(BN):
    sol = 0
    DFS(0, ball[i], 0)
    if sol:
        print('Y')
    else:
        print('N')
