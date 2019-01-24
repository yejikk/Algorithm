import sys
sys.stdin = open("특별한 정렬.txt")

def selectsort(N, numbers):
    for i in range(N):
        max = i
        min = i
        for j in range(i+1, N):
            # i가 짝수일 때는 max값 정렬
            if i % 2 == 0:
                if numbers[j] > numbers[max]:
                    max = j
            # i가 홀수일 때는 min값 정렬        
            else:
                if numbers[j] < numbers[min]:
                    min = j
        numbers[i], numbers[max] = numbers[max], numbers[i]
        numbers[i], numbers[min] = numbers[min], numbers[i]
    return numbers

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # for n in range(N):
    result = selectsort(N, numbers)[:10]
    result = ' '.join(map(str, result))
    print(f'#{tc} {result}')

