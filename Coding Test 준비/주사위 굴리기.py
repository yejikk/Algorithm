import sys
sys.stdin = open('주사위 굴리기.txt')

def wall(tx, ty):
    if tx < 0 or tx >= N or ty < 0 or ty >= M:
        return False
    return True

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))

print(bin(60)[2:])
print(type(bin(1)))
print('0' * 3)
print(format(9 | 30))
