a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(no, cnt): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
# 1] 리턴조건 : N번째이면 인쇄후 리턴
    # 2개만 들어가 있는 것만 print 하겠다.
    # if cnt == 2:
    #     for i in range(N):
    #         print(b[i], end=' ')
    #     print()
    #     return
    # 여기에 cnt 넣어줘도 됨. (편하게 하는 방법)
    if no >= N:
        for i in range(N):
            print(b[i], end=' ')
        print()
        return
# 2] 현재 구슬을 고르기(b배열에 담기)
    b[no] = a[no]
    DFS(no+1, cnt+1)
# 3] 현재 구슬을 고르지 않기(b배열에 담지 않기)
    b[no] = 0
    DFS(no+1, cnt) # 고르지 않았기 때문에 더하지 않음

# main ============================
DFS(0, 0) # a[0]요소 구슬부터 시작
