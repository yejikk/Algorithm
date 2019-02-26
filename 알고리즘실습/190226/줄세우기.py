import sys
sys.stdin = open('줄세우기.txt')

N = int(input())
number = list(map(int, input().split()))
student = []

for i in range(N):
    student.insert(number[i], i+1)
student.reverse()
print(' '.join(map(str, student)))
