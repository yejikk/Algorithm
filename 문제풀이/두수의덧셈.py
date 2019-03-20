import sys
sys.stdin = open('두수의덧셈.txt')

test = int(input())

for tc in range(1, test+1):
    A, B = map(str, input().split())

    if A[0] == 0:
        for i in range(len(A)):
            if A[i] != 0:
                A = A[i:]
                break

    if B[0] == 0:
        for j in range(len(B)):
            if B[j] != 0:
                B = B[i:]
                break

    print('#{} {}'.format(tc, int(A)+int(B)))