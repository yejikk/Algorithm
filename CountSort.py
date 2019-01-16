def countingSort(A, B, C):
    for i in range(len(A)):
        C[A[i]] += 1 # counting하고 있음 (궁금하면 디버깅 해보기)

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(A)-1, -1, -1 ):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

# 이 data 구현하기
A = [5, 8, 7, 1, 1, 5, 4, 1]
B = [0] * len(A)
C = [0] * 10
countingSort(A, B, C)
print(B)