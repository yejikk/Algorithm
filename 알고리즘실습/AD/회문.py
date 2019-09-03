import sys
sys.stdin = open('회문.txt')

def bruteforce(word):
    flag = 0

    for i in range(N-M+1):
        string = ''
        for j in range(M):
            string += word[i+j]

        string = list(map(str, string))
        re_string = reverse(string)

        if string == re_string:
            flag = 1
            return string

    if not flag:
        return -1

def reverse(string):
    text = string[:]
    for i in range(len(text)//2):
        temp = text[i]
        text[i] = text[len(text)-i-1]
        text[len(text)-i-1] = temp

    return text

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    for n in range(N):
        arr[n] = list(map(str, input()))

    flag = 0
    for i in range(N):
        result = bruteforce(arr[i])
        if result != -1:
            flag = 1
            break

    if not flag:
        for i in range(N):
            word = ''
            for j in range(N):
                word += arr[j][i]

            word = list(map(str, word))
            result = bruteforce(word)

            if result != -1:
                flag = 1
                break

    result = ''.join(result)
    print('#{} {}'.format(tc, result))

