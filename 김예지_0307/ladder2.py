import sys
sys.stdin = open('ladder2.txt')

def wall(tx, ty):
    if tx < 0 or tx >= 100:
        return False
    if ty < 0 or ty >= 100:
        return False
    if arr[tx][ty] == 0:
        return False
    return True

def ladder():
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    cntmin = 1000000
    result = 0
    stack = []
    for j in range(100):
        if arr[0][j] == 1:
            x = 0
            y = j
            stack.append([x, y])
    for t in stack:
        x = t[0]
        y = t[1]
        visited = []
        cnt = 0
        while x != 99:
            for i in range(3):
                tx = x + dx[i]
                ty = y + dy[i]
                if wall(tx, ty):
                    if [tx, ty] not in visited:
                        visited.append([tx, ty])
                        x = tx
                        y = ty
                        cnt += 1
        if cnt <= cntmin:
            cntmin = cnt
            result = t[1]

    return result

for tc in range(1, 11):
    T = input()
    arr = [[0]*100 for _ in range(100)]
    for k in range(100):
        arr[k] = list(map(int, input().split()))

    result = ladder()
    print('#' + str(tc) + ' ' + str(result))