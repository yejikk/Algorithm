'''
문제에서 거리를 구하는 공식이 주어졌으므로(공식이 있으므로 미로처럼 풀 이유가 없음),
while문을 통해서 1이 있는 곳을 계속 찾는것보다는
마을(=1)을 찾아서(for문 돌려서 list에 append 해줌) 기지국(=2)과의 거리를 거리구하는 공식을 통해서 구해준 뒤
최대값을 찾는다.(비교를 통해)
'''
import sys, math
sys.stdin = open('원안의마을.txt')

N = int(input())
arr =[[0]*N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

town = []
flag = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            x = i
            y = j
        elif arr[i][j] == 1:
            town.append([i, j])

result = 0
for i in range(len(town)):
    idx = town.pop()
    n = idx[0]
    m = idx[1]
    d = (((x-n)**2) + ((y-m)**2)) ** 0.5
    if d > result:
        result = d

print(math.ceil(result))
