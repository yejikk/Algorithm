"""
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1

정답 : 24
"""

def iswall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5 : return True
    return False
# 만약 함수를 쓰지 않는다면 return True 대신 continue를 쓴다.
def calAbs(y, x):
    if y-x > 0: return y-x
    else: return x-y

def myabs(a):
    if a > 0 : return a
    else: return -a

# arr = [[0 for _ in range(5)] for _ in range(5)]
#
# for i in range(5):
#     arr[i] = list(map(int, input().split()))

arr = [[1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1]]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4): # 상하좌우만 탐색하겠다는 의미
            testX = x + dx[i]
            testY = y + dy[i]
            if iswall(testX, testY) == False:
                # sum += calAbs(arr[y][x], arr[testY][testX])
                sum += abs(arr[y][x] - arr[testY][testX])

print(sum)