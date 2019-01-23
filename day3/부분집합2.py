arr = [1,2,3,4]
n = len(arr) # n : 원소의 개수

for i in range(1 << n): # 1<<n : 부분집합의 개수 <<(shift left가 2^n을 나타냄)
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i & (1 << j): # i의 j번째 비트가 1이면
            print(arr[j], end=' ') # j번째 원소 출력

    print()