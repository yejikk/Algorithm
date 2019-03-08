import sys
sys.stdin = open('나는학급회장이다.txt')

def diff():
    global president

N = int(input())
president = [[[] for _ in range(3)] for _ in range(3)]

for i in range(N):
    student = list(map(int, input().split()))
    print(student)
    # print(student)
    for j in range(3):
        if student[j] == 3:
            president[j][2].append(3)
        elif student[j] == 2:
            president[j][1].append(2)
        elif student[j] == 1:
            president[j][0].append(1)

score = [[0] for _ in range(3)]
for k in range(3):
    open = sum(president[k][0]) + sum(president[k][1]) + sum(president[k][2])
    score[k] = open
print(president)
print(score)
