import sys
sys.stdin = open('승률비교하기.txt')

test = int(input())
result = []

for tc in range(1, test+1):
    game = list(map(int, input().split()))
    if (game[1] / game[0]) > (game[3] / game[2]):
        result.append('#{} BOB'.format(tc))
    elif (game[1] / game[0]) < (game[3] / game[2]):
        result.append('#{} ALICE'.format(tc))
    elif (game[1] / game[0]) == (game[3] / game[2]):
        result.append('#{} DRAW'.format(tc))

print('\n'.join(result))