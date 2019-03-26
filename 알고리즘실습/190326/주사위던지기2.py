import sys
sys.stdin = open('주사위던지기2.txt')

def myprint(q):
    global M
    random = []
    while q:
        q -= 1
        random.append(t[q])
    if sum(random) == M:
        result.append(random)
def perm(n, r, q):
    if r == 0:
        myprint(q)
    else:
         for i in range(n-1, -1, -1):
             num[i], num[n-1] = num[n-1], num[i]
             t[r-1] = num[n-1]
             perm(n, r-1, q)
             num[i], num[n-1] = num[n-1], num[i]

N, M = map(int, input().split())

num = [1, 2, 3, 4, 5, 6]
result = []
t = [0] * N
perm(6, N, N)
result.sort()
for i in range(len(result)):
    print(' '.join(map(str, result[i])))
# print(result)