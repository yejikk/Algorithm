def DFS(no, cnt):
    if no >= N:
        for i in range(N):
            print(b[i], end=' ')
        print()
        return

    b[no] = a[no]
    DFS(no+1, cnt+1)
    b[no] = 0
    DFS(no+1, cnt)

a = [2, 5, 7] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3
DFS(0, 0) # a[0]요소 구슬부터 시작