import sys
sys.stdin = open('초콜릿공장.txt')

def choco(A, B):
    cnt = 0
    for a in A:
        if a in B:
            cnt += 1
    if cnt > 2:
        return 1
    else:
        return 0

def Acompany(A):
    acnt = 0
    for a in A:
        if A.count(a) > 1:
            acnt += 1
            break
    if acnt > 0:
        return 1
    else:
        return 0

def Bcompany(B):
    bcnt = 0
    for b in B:
        if B.count(b) > 1:
            bcnt += 1
            break
    if bcnt > 0:
        return 1
    else:
        return 0

N = int(input())

result = 0
for i in range(N):
    A, B = map(str, input().split())
    if choco(A, B) or Acompany(A) or Bcompany(B):
        result += 1

print(result)
