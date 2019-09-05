import sys
sys.stdin = open('자동차경주대회.txt')

K = int(input())
N = int(input())

stop = list(map(int, input().split()))
time = list(map(int, input().split()))

