# 가지수를 세기위해서 check list를 만들어서 check
# 쿠폰을 먹었는지 안먹었는지 check list 확인해보기
# 슬라이딩 기법
'''
계속 이어가는 것이 아니라 초밥을 새로 먹는다고 생각하고 문제풀기
'''
# cnt, type
import sys
sys.stdin = open('회전초밥.txt')

N, d, k, c = map(int, input().split())
dish = []
check = [0] * (d + 1)
for i in range(N):
    dish.append(int(input()))

sol = 0
for i in range(N):
    for j in range(k):
        check[dish[(i + j) % N]] = 1
    cnt = 0
    if check[c] == 0:
        cnt = 1
    for j in range(1, d + 1):
        cnt += check[j]
        check[j] = 0
    if cnt > sol:
        sol = cnt
print(sol)