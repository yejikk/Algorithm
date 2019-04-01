import sys
sys.stdin = open('상자포장하기.txt')

def DFS(no, lastA, lastB, hap):
    global sol
    if no >= N:
        if hap > sol:
            sol = hap
        return

    # A : 작은 상자 순으로 포장하기
    if lastA > arr[no]:
        DFS(no+1, arr[no], lastB, hap+arr[no])

    # B : 큰 상자 순으로 포장하기
    if lastB < arr[no]:
        DFS(no+1, lastA, arr[no], hap+arr[no])

    DFS(no+1, lastA, lastB, hap)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sol = 0
    DFS(0, 1000, 0, 0)
    print(sol)