import sys
sys.stdin = open("문자열 비교_input.txt")

test = int(input())


def brute(str1, str2):
    for i in range(len(str2) - len(str1) + 1):
        cnt = 0
        for j in range(len(str1)):
            if str2[i + j] != str1[j]:
                break
            else:
                cnt += 1
        if cnt == len(str1):
            return 1
    return 0


for tc in range(1, test + 1):
    str1 = input()
    str2 = input()

    result = brute(str1, str2)
    print(f'#{tc} {result}')