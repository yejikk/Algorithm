# 재귀 호출을 통한 순열 생성
# 외우는 것이 좋음

def perm(n, k):
    if n == k:
        print(a)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i] # swap
            perm(n, k+1)
            a[i], a[k] = a[k], a[i] # swap 되돌리기

a = [1, 2, 3]
perm(3, 0)