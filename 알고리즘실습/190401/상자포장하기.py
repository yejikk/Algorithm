import sys
sys.stdin = open('상자포장하기.txt')

# 마지막에 포장된 정보를 가지고 다녀야함
# 시작이 매 번 바뀜 (A는 min 비교로 시작해야함, B는 max 비교로 시작해야함)
# 이중 재귀

def DFS(no, k):
    global maxsum
    if no == k:
        A = []
        B = []
        for i in range(N):
            if temp[i] == 1:
                A.append(box[i])
            else:
                B.append(box[i])
        print(A)
        print(B)
        print(B)
        Acnt = 0
        Bcnt = 0
        for n in range(1, len(A)):
            if A[n-1] < A[n]:
                break
            else:
                Acnt += A[n-1]
        if Acnt:
            Acnt += A[-1]
        for m in range(1, len(B)):
            if B[m-1] > B[m]:
                break
            else:
                Bcnt += B[m-1]
        if Bcnt:
            Bcnt += B[-1]

        total = Acnt + Bcnt
        if total > maxsum:
            maxsum = total

    else:
        temp[k] = 1
        DFS(no, k+1)
        temp[k] = 0
        DFS(no, k+1)

test = int(input())

for tc in range(test):
    N = int(input())
    box = list(map(int, input().split()))
    temp = [0] * N
    # print(box)
    maxsum = 0
    DFS(N, 0)
    print(maxsum)