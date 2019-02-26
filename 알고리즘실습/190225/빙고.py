import sys
sys.stdin = open('빙고.txt')

def check(bingo, number):
    flag = 0
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                bingo[i][j] = 0
                flag = 1
                break
        if flag == 1:
            break
    return bingo

def win(bingo):
    flag = 1
    line = 0
    if flag:
        for i in range(5):
            rowsum = 0
            for j in range(5):
                rowsum += bingo[i][j]
            if rowsum == 0:
                line += 1
                if line == 3:
                    flag = 0
                    break
            if flag == 0:
                break

    if flag:
        for i in range(5):
            colsum = 0
            for j in range(5):
                colsum += bingo[j][i]
            if colsum == 0:
                line += 1
                if line == 3:
                    flag = 0
                    break
            if flag == 0:
                break
    if flag:
        cross = 0
        for i in range(5):
            cross += bingo[i][j]
        if cross == 0:
            line += 1
            if line == 3:
                flag = 0

    if flag:
        back = 0
        for i in range(5):
            back += bingo[4-i][i]
        if back == 0:
            line += 1
            if line == 3:
                flag = 0

    return line

bingo = [[0]*5 for _ in range(5)]
for i in range(5):
    bingo[i] = list(map(int, input().split()))
num = [[0]*5 for _ in range(5)]
for j in range(5):
    num[j] = list(map(int, input().split()))
cnt = 0
line = 0
flag = 0

for i in range(5):
    for j in range(5):
        check(bingo, num[i][j])
        cnt += 1
        line = win(bingo)
        if line == 3:
            flag = 1
            break
    if flag:
        break

print(cnt)