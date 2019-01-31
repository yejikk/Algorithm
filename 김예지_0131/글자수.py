import sys
sys.stdin = open("글자수_input.txt")

test = int(input())

for tc in range(1, test+1):
    str1 = input()
    str2 = input()
    max = 0

    for char1 in str1:
        cnt = 0
        for char2 in str2:
            if char1 == char2:
                cnt += 1
        if cnt > max:
            max = cnt

    print(f'#{tc} {max}')