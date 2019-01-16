def BubbleSort(data):
    for i in range(len(data)-1, 0, -1): # 4 ~ 1 (큰 for문 4번 돔)
        for j in range(0, i): # 0 ~ 3
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

data = [5, 4, 3, 2, 1]
BubbleSort(data)
print(data)

# call by value : 복사
# call by reference : 원본 참조
# 재귀함수를 많이 쓰면 stack overflow가 생김(Heap)