import sys
sys.stdin = open('문자열비교.txt')

def bruteforce(str1, str2):
    flag = 0

    for i in range(len(str2)-len(str1)+1):
        cnt = 0
        for j in range(len(str1)):
            if str2[i+j] != str1[j]:
                break
            else:
                cnt += 1

            if cnt == len(str1):
                flag = 1
                break
        if flag:
            break

    if flag:
        return 1
    else:
        return 0

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print('#{} {}'.format(tc, bruteforce(str1, str2)))
