import sys
sys.stdin = open('특별한정렬.txt')

# selection sort
def sort_num(numbers):
    for i in range(N):
        # 초기 index 저장
        max_idx = i
        min_idx = i
        for j in range(i+1, N):
            if i % 2 == 0:
                if numbers[max_idx] < numbers[j]:
                    max_idx = j
            else:
                if numbers[min_idx] > numbers[j]:
                    min_idx = j

        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = sort_num(numbers)[:10]
    result = ' '.join(map(str, result))

    print('#{} {}'.format(tc, result))
