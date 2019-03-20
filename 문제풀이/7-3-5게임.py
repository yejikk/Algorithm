import sys
sys.stdin = open('7-3-5게임.txt')

test = int(input())

for tc in range(1, test+1):
    number = list(map(int, input().split()))
    result = []
    for i in range(7-3+1):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                numsum = number[i]
                numsum += number[j]
                numsum += number[k]
                result.append(numsum)
    result = list(set(result))
    result.sort()
    result.reverse()
    print(f'#{tc} {result[4]}')
