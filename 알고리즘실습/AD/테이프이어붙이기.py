import sys
sys.stdin = open('테이프이어붙이기.txt')

def dfs(no, cnt, nsum):
    global nmin

    if cnt + (N-no) < N//2:
        return

    if no >= N:
        return

    if cnt == (N//2):
        print(temp, nsum)
        num = abs(nsum - (tot - nsum))
        if num < nmin:
            nmin = num
        return

    temp[no] = tape[no]
    dfs(no+1, cnt+1, nsum+tape[no])

    temp[no] = 0
    dfs(no+1, cnt, nsum)

N = int(input())
tape = list(map(int, input().split()))
temp = [0]*N

tot = sum(tape)
nmin = 100000000
dfs(0, 0, 0)
print(nmin)