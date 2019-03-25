import sys
sys.stdin = open('예산.txt')

N = int(input())
budget = list(map(int, input().split()))
limit = int(input())
