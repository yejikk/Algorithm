# 재귀를 이용한 선택정렬

def SelectionSort(num, s, e):
    mini = s

    # 반복문 조건이 0 ~ len(number)-1이기 때문에
    # 처음과 끝이 같아지면 return 한다.
    if s == e:
        return

    for i in range(s+1, e):
        if num[i] < num[mini]:
            mini = i

    num[s], num[mini] = num[mini], num[s]
    SelectionSort(num, s+1, e)

number = [8, 3, 5, 9, 1, 2, 7]
SelectionSort(number, 0, len(number))
print(number)