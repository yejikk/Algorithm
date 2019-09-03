import sys
sys.stdin = open('종이붙이기.txt')

# 재귀로 푸는 문제
T = int(input())

for tc in range(1, T+1):
    N = int(input())