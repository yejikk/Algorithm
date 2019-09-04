def DFS(n):
    if n >= N:
        for i in range(N):
            print(b[i], end=' ')
        print()

        return

    for i in range(N):
        b[n] = a[i]
        if chk[i]:
            continue
        chk[i] = 1
        DFS(n+1)
        chk[i] = 0

a = [2, 5, 7] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
chk = [0, 0, 0] # 구슬 사용여부 체크
N = 3
DFS(0)
