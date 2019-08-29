def printSet(n, nsum):
    global count
    count += 1
    result = []
    if nsum == 10:
        for i in range(n):
            if a[i] == 1:
                result.append(number[i])
    if result:
        print(result)

def powerset(n, k, nsum):
    global N
    if nsum > 10:
        return
    
    if n == k:
        printSet(n, nsum)
        # for i in range(N):
        #     if a[i] == 1:
        #         print(number[i], end=' ')
        # print('끝')
    else:
        a[k] = 1 # k번 요소가 있음
        powerset(n, k+1, nsum + number[k])
        a[k] = 0 # k번 요소가 없음
        powerset(n, k+1, nsum)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
N = 10
a = [0 for _ in range(N)]

powerset(N, 0, 0)