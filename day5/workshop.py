import sys
sys.stdin = open('workshop.txt')

def two(arr):
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                x = i
                y = j
                return x, y

for tc in range(10):
    case = input()
    arr = [[0]*100 for _ in range(100)]

    for i in range(100):
        arr[i] = list(map(int, input().split()))

    x, y = two(arr)

    '''
    2를 먼저 찾아주고 올라가는 방식
    함수 two를 사용해서 2가 있는 행과 열을 찾아줘서 x, y에 넣어서 return해준다.
    만약, y가 0이라면 이동할 수 있는 곳이 위와 오른쪽밖에 없기 때문에 예외처리해준다. 
    (또한 out of range가 발생하기 때문에 꼭 예외처리를 해줘야한다.)
    만약, y가 99라면 이동할 수 있는 곳이 위와 왼쪽밖에 없기 때문에 예외처리해준다.
    (이것 또한 out of range가 발생할 수 있다.)
    모든 탐색은 위가 1인지 부터 검사해서 x의 index를 위로 올려주고(-1을 해서), 
    그 다음 왼쪽이 1인지 오른쪽이 1인지 검사한다. 
    왼쪽, 오른쪽 모두 1일 수도 있기 때문에 지나온 곳은 꼭 0으로 바꿔서 방향설정에 어려움을 겪지 않게 한다.
    '''

    while x > 0 and (y >= 0 and y < 100):
        if y == 0:
            if arr[x-1][y] == 1:
                x -= 1
                arr[x][y] = 0

            if arr[x][y+1] == 1:
                y += 1
                arr[x][y] = 0

        elif y == 99:
            if arr[x-1][y] == 1:
                x -= 1
                arr[x][y] = 0

            if arr[x][y-1] == 1:
                y -= 1
                arr[x][y] = 0

        else:
            if arr[x-1][y] == 1:
                x -= 1
                arr[x][y] = 0

            if arr[x][y-1] == 1:
                y -= 1
                arr[x][y] = 0

            elif arr[x][y+1] == 1:
                y += 1
                arr[x][y] = 0

    print(f'#{case} {y}')


