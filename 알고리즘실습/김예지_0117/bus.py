import sys
sys.stdin = open("bus.txt")

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    stop = [0] * (N+1) # 버스 정류장
    power = [0] * K # 충전 가능한 정류장
    cnt = 0 # 충전 횟수

    for n in range(len(stop)):
        stop[n] += n
    print(stop)

    for m in range(len(charge)):
        power[charge[m]] += 1
    print(power)

    for i in range