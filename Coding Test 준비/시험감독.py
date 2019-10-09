import sys
sys.stdin = open('시험감독.txt')

N = int(input())
students = list(map(int, input().split()))
total, sub = map(int, input().split())
result = 0

for stu in students:
    if (stu - total) <= 0:
        result += 1
    else:
        result += 1
        stu -= total
        q = stu // sub
        p = stu % sub
        if p > 0:
            result += (q + 1)
        else:
            result += q

print(result)