import sys
sys.stdin = open('최소비용포장.txt')

def Qsort(s, e):
    global N, candy
    if s >= e:
        return
    P = e
    T = s
    for L in range(s, e+1):
        if candy[L] < candy[P]:
            candy[L], candy[T] = candy[T], candy[L]
            T += 1
    candy[T], candy[P] = candy[P], candy[T]
    Qsort(s, T - 1)
    Qsort(T + 1, e)

N = int(input())
candy = list(map(int, input().split()))
cnt = 0

i = 0
while len(candy) >= 2:
    c = candy[i] + candy[i+1]
    cnt += c
    candy.pop(0)
    candy.pop(0)
    candy.insert(0, c)
    Qsort(0, len(candy)-1)

print(cnt)

# N = int(input())
# candy = list(map(int, input().split()))
#
# cnt = 0
# for k in range(N-1):
#     for i in range(k, k+2):
#         for j in range(i+1, N):
#             if candy[i] > candy[j]:
#                 candy[i], candy[j] = candy[j], candy[i]
#
#     candy[k+1] += candy[k]
#     cnt += candy[k+1]
# print(cnt)