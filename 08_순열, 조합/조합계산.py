def comb(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return comb(n-1, r-1) + comb(n-1, r)
        # 재귀로 하는 이유는 가지치기를 하기 위해서
print(comb(4, 3))