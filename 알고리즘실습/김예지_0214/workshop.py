import sys
sys.stdin = open('workshop.txt')

def work(v):
    stack.append(v)
    while len(stack) != 0:
        v = stack.pop()

# 다시 index 찾아주는 함수
def index():

# 위상정렬방법 이용해서 풀기

for tc in range(1):
    V, E = map(int, input().split())
    route = [[0]*(V+1) for _ in range(V+1)]
    temp = list(map(int, input().split()))
    num = [0] * (V+1)
    stack = []

    for i in range(E):
        route[temp[i*2]][temp[i*2+1]] = 1

    for j in range(E):
        num[temp[j*2+1]] += 1

    for n in range(1, len(num)):
        if num[n] == 0:
            v = n
            break

    # work(v)
    print(num)
    print(v)

