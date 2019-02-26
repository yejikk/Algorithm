import sys
sys.stdin = open('폭탄돌리기.txt')

start = int(input())
quiz = int(input())
total = 0
flag = 0

while quiz:
    quiz -= 1
    time, ans = input().split()
    if ans == 'T':
        total += int(time)
        if total >= 210:
            flag = 1
            break
        else:
            start += 1

    elif ans == 'F' or ans == 'P':
        total += int(time)
        if total >= 210:
            flag = 1
            break

if flag:
    person = start % 8
    if person == 0:
        person = 8
    print(person)

elif total < 210 and flag == 0:
    person = start % 8
    if person == 0:
        person = 8
    print(person)

