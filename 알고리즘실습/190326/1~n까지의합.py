import sys
sys.stdin = open('1~n까지의합.txt')

def numsum(n):
    if n <= 1:
        return 1
    else:
        return n + numsum(n-1)

N = int(input())
result = numsum(N)
print(result)