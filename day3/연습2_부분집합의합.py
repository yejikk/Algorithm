"""
10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를
계산하는 함수를 작성해보자.
"""

# 빈 list말고 sum을 만들어서 직접 더해서 구해보기 (함수도 만들어보기)

arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]

flag = 0

for i in range(1, 1<<len(arr)):
    result = []
    for j in range(len(arr)):
        if i & (1 << j):
            result.append(arr[j])
    if sum(result) == 0:
        flag += 1
print(flag)