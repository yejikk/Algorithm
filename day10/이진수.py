import sys
sys.stdin = open('이진수.txt')

def aToh(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

test = int(input())

for tc in range(1, test+1):
    N, number = map(str, input().split())
    asc = [[0, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0],
           [0, 0, 1, 1],
           [0, 1, 0, 0],
           [0, 1, 0, 1],
           [0, 1, 1, 0],
           [0, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 1],
           [1, 0, 1, 0],
           [1, 0, 1, 1],
           [1, 1, 0, 0],
           [1, 1, 0, 1],
           [1, 1, 1, 0],
           [1, 1, 1, 1]]

    t = []
    for i in range(len(number)):
        makeT(aToh(number[i]))

    t = ''.join(map(str, t))
    print(f'#{tc} {t}')