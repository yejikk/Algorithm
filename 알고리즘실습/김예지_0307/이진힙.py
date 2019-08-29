import sys
sys.stdin = open('이진힙.txt')

def enQ(n):
    global last
    last += 1 # 마지막 노드번호 증가
    c = last # 마지막 노드를 자식 노드로
    p = c // 2 # 부모 노드 번호 계산
    Q[last] = n # 마지막 노드에 값 저장
    while c > 1 and Q[p] > Q[c]:
        t = Q[p]
        Q[p] = Q[c]
        Q[c] = t
        c = p
        p //= 2

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    number = list(map(int, input().split()))
    Q = [0 for _ in range(N+1)]
    last = 0

    for i in range(N):
        enQ(number[i])

    i = (len(Q)-1) // 2
    result = 0
    while True:
        result += Q[i] # 모든 조상 값 더하기
        i //= 2
        if i == 0:
            break

    print('#' + str(tc) + ' ' + str(result))