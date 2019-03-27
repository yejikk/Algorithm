# 재귀 호출로 순열을 이용해서 문제를 품

# a = [1, 2, 4, 7, 8, 3]
a = [1, 2, 3, 4, 4, 4]

def babyGin():
    global flag
    check = 0

    if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
        check += 1
    if a[3] + 1 == a[4] and a[4] + 1 == a[5]:
        check += 1

    if a[0] == a[1] and a[1] == a[2]:
        check += 1
    if a[3] == a[4] and a[4] == a[5]:
        check += 1

    if check == 2:
        flag = 1
        return

def perm(n, k):
    if n == k:
        babyGin()
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i] # swap
            perm(n, k+1)
            a[i], a[k] = a[k], a[i] # swap 되돌리기

flag = 0
perm(6, 0)

if flag:
    print('Babygin')
else:
    print('Not babygin')