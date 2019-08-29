# 재귀를 이용한 선택정렬

def SelectionSort(num):
    n = len(num)
    for i in range(0, n-1):
        nmin = i
        for j in range(i+1, n):
            if num[j] < num[nmin]:
                nmin = j
        num[i], num[nmin] = num[nmin], num[i]

    return num

number = [8, 3, 5, 9, 1, 2, 7]
print(SelectionSort(number))