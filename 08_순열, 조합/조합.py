def myprint(q):
    while q != 0:
        q = q - 1
        print('{}'.format(T[q]), end=' ')
    print()

# 이 함수에 가지치기를 한다.
def comb(n, r, q):
    if r == 0:
        myprint(q)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)

A = [1, 2, 3, 4]
T = [0] * 3
comb(4, 3, 3)