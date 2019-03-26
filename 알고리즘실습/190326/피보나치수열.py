import sys
sys.stdin = open('피보나치수열.txt')

def fibo(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b

N = int(input())
result = fibo(N)
print(result)