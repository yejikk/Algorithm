import sys
sys.stdin = open('주사위던지기2.txt')

def DFS(no, nsum):
    if no > N:
        if nsum == M:
            for i in range(1, N+1):
                print(temp[i], end=' ')
            print()
        return

    for i in range(1, 7):
        temp[no] = i
        DFS(no+1, nsum + temp[no]) # DFS 재귀

N, M = map(int, input().split())
temp = [0] * 7
DFS(1, 0) # 시작점, nsum