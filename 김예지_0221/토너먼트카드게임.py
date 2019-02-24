import sys
sys.stdin = open('토너먼트카드게임.txt')

test = int(input())

def win(left, right):
    if (left[0][1] == right[0][1]) or (left[0][1] == 1 and right[0][1] == 3) or (left[0][1] == 2 and right[0][1] == 1) or (left[0][1] == 3 and right[0][1] == 2):
        return left[0]
    elif (right[0][1] == 1 and left[0][1] == 3) or (right[0][1] == 2 and left[0][1] == 1) or (right[0][1] == 3 and left[0][1] == 2):
        return right[0]

def tournament(left, right):
    if len(left) == 1 and len(right) == 1:
        return win(left, right)
    else:
        if len(left) > 1:
            stuleft = left[:(len(left)+1)//2]
            sturight = left[(len(left)+1)//2:]
            left = list([tournament(stuleft, sturight)])

        elif len(right) > 1:
            stuleft = right[:(len(right)+1)//2]
            sturight = right[(len(right)+1)//2:]
            right = list([tournament(stuleft, sturight)])
    return tournament(left, right)

for tc in range(1, test+1):
    N = int(input())
    student = list(map(int, input().split()))
    for i in range(N):
        student[i] = [i+1, student[i]]

    left = student[:(N+1)//2]
    right = student[(N+1)//2:]

    winner = tournament(left, right)
    print(f'#{tc} {winner[0]}')


