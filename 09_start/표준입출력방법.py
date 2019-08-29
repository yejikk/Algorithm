import sys
sys.stdin = open('표준입출력방법.txt')

test = int(input())
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

print(test)
print(N, M)
for j in range(N):
    arr[j] = ''.join(map(str, arr[j]))
    print(arr[j])
