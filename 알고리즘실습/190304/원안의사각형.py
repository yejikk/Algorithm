import sys
sys.stdin = open('원안의사각형.txt')

N = int(input())
result = 0

for i in range(N):
    for j in range(N):
        if ((N-i)**2) + ((N-j)**2) <= N**2:
            result += N - j
            break
result *= 4
print(result)