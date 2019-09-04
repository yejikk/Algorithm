def myprint(q):
    while q:
        q -= 1
        print('{}'.format(t[q]), end=' ')
    print()

def perm(n, r, q):
    if r == 0:
        myprint(q)
    else:
         for i in range(n):
             a[i], a[n-1] = a[n-1], a[i]
             t[r-1] = a[n-1]
             perm(n-1, r-1, q)
             a[i], a[n-1] = a[n-1], a[i]

a = [1, 2, 3]
t = [0] * 3
perm(3, 3, 3)