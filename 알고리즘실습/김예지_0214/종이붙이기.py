import sys
sys.stdin = open('종이붙이기.txt')

def rectangle(num):
    for i in range(2, num+1):
        # 10씩 늘어날 때, 가로의 경우와 세로의 경우를 따져서 계산해줌
        square.append(square[i-1] + 2*square[i-2])
    return square[num-1]

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    num = N // 10
    square = [1, 3]
    result = rectangle(num)
    print(f'#{tc} {result}')
